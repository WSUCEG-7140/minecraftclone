import nbtlib as nbt
import base36
import logging

import chunk
import glm

class Save:
    def __init__(self, world, path="save"):
        self.world = world
        self.path = path

    def chunk_position_to_path(self, chunk_position):
        x, _, z = chunk_position

        # Generate the chunk file path based on chunk position
        chunk_path = '/'.join((self.path,
                               base36.dumps(x % 64), base36.dumps(z % 64),
                               f"c.{base36.dumps(x)}.{base36.dumps(z)}.dat"))

        return chunk_path

    def load_chunk(self, chunk_position):
        logging.debug(f"Loading chunk at position {chunk_position}")
        
        # Load the chunk file
        chunk_path = self.chunk_position_to_path(chunk_position)
        try:
            chunk_blocks = nbt.load(chunk_path)["Level"]["Blocks"]
        except FileNotFoundError:
            return

        # Create a new chunk and fill it with blocks from the chunk file
        self.world.chunks[glm.ivec3(chunk_position)] = chunk.Chunk(self.world, glm.ivec3(chunk_position))

        for x in range(chunk.CHUNK_WIDTH):
            for y in range(chunk.CHUNK_HEIGHT):
                for z in range(chunk.CHUNK_LENGTH):
                    self.world.chunks[glm.ivec3(chunk_position)].blocks[x][y][z] = chunk_blocks[
                        x * chunk.CHUNK_LENGTH * chunk.CHUNK_HEIGHT +
                        z * chunk.CHUNK_HEIGHT +
                        y]

    def save_chunk(self, chunk_position):
        logging.debug(f"Saving chunk at position {chunk_position}")
        x, y, z = chunk_position

        # Try to load the chunk file, if it doesn't exist, create a new one
        chunk_path = self.chunk_position_to_path(chunk_position)
        try:
            chunk_data = nbt.load(chunk_path)
        except FileNotFoundError:
            chunk_data = nbt.File({"": nbt.Compound({"Level": nbt.Compound()})})
            chunk_data["Level"]["xPos"] = x
            chunk_data["Level"]["zPos"] = z

        # Fill the chunk file with the blocks from the chunk
        chunk_blocks = nbt.ByteArray([0] * (chunk.CHUNK_WIDTH * chunk.CHUNK_HEIGHT * chunk.CHUNK_LENGTH))

        for x in range(chunk.CHUNK_WIDTH):
            for y in range(chunk.CHUNK_HEIGHT):
                for z in range(chunk.CHUNK_LENGTH):
                    chunk_blocks[
                        x * chunk.CHUNK_LENGTH * chunk.CHUNK_HEIGHT +
                        z * chunk.CHUNK_HEIGHT +
                        y] = self.world.chunks[chunk_position].blocks[x][y][z]

        # Save the chunk file
        chunk_data["Level"]["Blocks"] = chunk_blocks
        chunk_data.save(chunk_path, gzipped=True)

    def load(self):
        logging.info("Loading world")

        # Load chunks in the specified range
        for x in range(-4, 4):
            for y in range(-4, 4):
                self.load_chunk((x, 0, y))

        for x in range(-1, 1):
            for y in range(-1, 1):
                self.load_chunk((x, 0, y))

        # Increase light for blocks in the world's light_blocks set
        for chunk_position, unlit_chunk in self.world.chunks.items():
            for x in range(chunk.CHUNK_WIDTH):
                for y in range(chunk.CHUNK_HEIGHT):
                    for z in range(chunk.CHUNK_LENGTH):
                        if unlit_chunk.blocks[x][y][z] in self.world.light_blocks:
                            world_pos = glm.ivec3(
                                chunk_position[0] * chunk.CHUNK_WIDTH + x,
                                chunk_position[1] * chunk.CHUNK_HEIGHT + y,
                                chunk_position[2] * chunk.CHUNK_LENGTH + z
                            )
                            self.world.increase_light(world_pos, 15, False)

    def save(self):
        logging.info("Saving world")
        
        # Save modified chunks to chunk files
        for chunk_position in self.world.chunks:
            if chunk_position[1] != 0:  # Reject all chunks above and below the world limit
                continue

            chunk = self.world.chunks[chunk_position]

            if chunk.modified:
                self.save_chunk(chunk_position)
                chunk.modified = False
#test cases 
class TestSave(unittest.TestCase):
    def setUp(self):
        self.world = World()  # Assuming World class is defined elsewhere
        
        # Initialize the Save instance with a mock world and path
        self.save = Save(self.world, "save")

    def test_chunk_position_to_path(self):
        chunk_position = (10, 0, 5)
        expected_path = "save/a.b/c.c.dat"

        path = self.save.chunk_position_to_path(chunk_position)
        self.assertEqual(path, expected_path)

    def test_load_chunk_existing_file(self):
        chunk_position = (10, 0, 5)
        chunk_path = "save/a.b/c.c.dat"
        chunk_data = nbt.File({"Level": {"Blocks": [1, 2, 3]}})
        expected_chunk = Chunk(self.world, glm.ivec3(chunk_position))

        with patch("nbtlib.load", return_value=chunk_data):
            self.save.load_chunk(chunk_position)
        
        self.assertEqual(self.world.chunks[glm.ivec3(chunk_position)], expected_chunk)

    def test_load_chunk_non_existing_file(self):
        chunk_position = (20, 0, 15)
        chunk_path = "save/d.e/f.f.dat"

        with patch("nbtlib.load", side_effect=FileNotFoundError):
            self.save.load_chunk(chunk_position)

        # Ensure no chunk is loaded
        self.assertNotIn(glm.ivec3(chunk_position), self.world.chunks)

    def test_save_chunk_existing_file(self):
        chunk_position = (10, 0, 5)
        chunk_path = "save/a.b/c.c.dat"
        chunk_data = nbt.File({"Level": {"Blocks": [4, 5, 6]}})

        with patch("nbtlib.load", return_value=chunk_data):
            with patch("nbtlib.save") as mock_save:
                self.save.save_chunk(chunk_position)

        mock_save.assert_called_once_with(chunk_path, gzipped=True)
        self.assertFalse(self.world.chunks[glm.ivec3(chunk_position)].modified)

    def test_save_chunk_non_existing_file(self):
        chunk_position = (20, 0, 15)
        chunk_path = "save/d.e/f.f.dat"
        chunk_data = nbt.File({"Level": {}})

        with patch("nbtlib.load", side_effect=FileNotFoundError):
            with patch("nbtlib.save") as mock_save:
                self.save.save_chunk(chunk_position)

        mock_save.assert_called_once_with(chunk_path, gzipped=True)
        self.assertFalse(self.world.chunks[glm.ivec3(chunk_position)].modified)

    def test_load(self):
        # Test case for load() method
        pass

    def test_save(self):
        # Test case for save() method
        pass

if __name__ == "__main__":
    unittest.main()
