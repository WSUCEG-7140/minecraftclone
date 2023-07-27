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

