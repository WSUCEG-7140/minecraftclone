import options
import pyglet
import logging

import pyglet.gl as gl

class TextureManager:
	def __init__(self, texture_width, texture_height, max_textures):
		# Initialize texture manager with provided width, height, and max number of textures
		self.texture_width = texture_width
		self.texture_height = texture_height
		self.max_textures = max_textures

		# Create an empty list to store the loaded texture names
		self.textures = []

		# Generate and bind a new OpenGL texture array
		self.texture_array = gl.GLuint(0)
		gl.glGenTextures(1, self.texture_array)
		gl.glBindTexture(gl.GL_TEXTURE_2D_ARRAY, self.texture_array)

		# Set texture filtering options for the texture array using mipmap type defined in options
		gl.glTexParameteri(gl.GL_TEXTURE_2D_ARRAY, gl.GL_TEXTURE_MIN_FILTER, options.MIPMAP_TYPE)
		gl.glTexParameteri(gl.GL_TEXTURE_2D_ARRAY, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)

		# Allocate storage for the texture array with specified width, height, and max number of textures
		gl.glTexImage3D(
			gl.GL_TEXTURE_2D_ARRAY, 0, gl.GL_RGBA,
			self.texture_width, self.texture_height, self.max_textures,
			0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, None)
	
	def generate_mipmaps(self):
		# Generate mipmaps for the texture array using the mipmap type specified in options
		logging.debug(f"Generating Mipmaps, using mipmap type {options.MIPMAP_TYPE}")
		gl.glGenerateMipmap(gl.GL_TEXTURE_2D_ARRAY)
	
	def add_texture(self, texture):
		# Load a new texture and add it to the texture manager
		logging.debug(f"Loading texture textures/{texture}.png")

		# If the texture is not already in the textures list, add it
		if not texture in self.textures:
			self.textures.append(texture)

			# Load the texture image and get image data
			texture_image = pyglet.image.load(f"textures/{texture}.png").get_image_data()
			gl.glBindTexture(gl.GL_TEXTURE_2D_ARRAY, self.texture_array)

			# Update the corresponding layer in the texture array with the loaded texture
			gl.glTexSubImage3D(
				gl.GL_TEXTURE_2D_ARRAY, 0,
				0, 0, self.textures.index(texture),
				self.texture_width, self.texture_height, 1,
				gl.GL_RGBA, gl.GL_UNSIGNED_BYTE,
				texture_image.get_data("RGBA", texture_image.width * 4))
#testcases
class TestTextureManager(unittest.TestCase):
    def setUp(self):
        # Initialize necessary variables here (e.g., texture_width, texture_height, max_textures)
        self.texture_width = 64
        self.texture_height = 64
        self.max_textures = 10

        # You may also set up a mock logger if needed for testing logging statements

    def test_texture_manager_init(self):
        # Test TextureManager initialization
        texture_manager = TextureManager(self.texture_width, self.texture_height, self.max_textures)

        # Assert that the textures list is empty after initialization
        self.assertEqual(len(texture_manager.textures), 0)

        # Assert that the texture_array is not None
        self.assertIsNotNone(texture_manager.texture_array)

    def test_generate_mipmaps(self):
        # Test generating mipmaps
        texture_manager = TextureManager(self.texture_width, self.texture_height, self.max_textures)

        # Generate mipmaps
        texture_manager.generate_mipmaps()

        # Perform assertions for the success of mipmaps generation (e.g., check if mipmap option is set)

    def test_add_texture(self):
        # Test adding a texture
        texture_manager = TextureManager(self.texture_width, self.texture_height, self.max_textures)

        # Load a sample texture for testing (you may need to prepare the required image for this test)
        sample_texture = "sample_texture"
        pyglet.image.get_image_data = lambda: pyglet.image.ImageData(
            self.texture_width, self.texture_height, 'RGBA', (self.texture_width * 4), b'')

        # Add the sample texture
        texture_manager.add_texture(sample_texture)

        # Assert that the texture is added to the textures list
        self.assertIn(sample_texture, texture_manager.textures)

        # Perform assertions for the texture_array after adding the texture (e.g., check if texture is correctly loaded)

    def test_add_existing_texture(self):
        # Test adding an existing texture
        texture_manager = TextureManager(self.texture_width, self.texture_height, self.max_textures)

        # Add a sample texture
        sample_texture = "sample_texture"
        texture_manager.add_texture(sample_texture)

        # Add the same texture again
        texture_manager.add_texture(sample_texture)

        # Assert that the texture is not added again to the textures list
        self.assertEqual(texture_manager.textures.count(sample_texture), 1)

        # Perform assertions for the texture_array after adding the existing texture (e.g., check if it remains unchanged)

    # Add more test cases as needed to cover other scenarios

if __name__ == '__main__':
    unittest.main()
