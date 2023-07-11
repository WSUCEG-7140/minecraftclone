import ctypes
import pyglet.gl as gl

import glm

class Shader_error(Exception):
	def __init__(self, message):
		self.message = message

def create_shader(target, source_path):
	# read shader source

	with open(source_path, "rb") as source_file:
		source = source_file.read()


	source_length = ctypes.c_int(len(source) + 1)
	source_buffer = ctypes.create_string_buffer(source)

	buffer_pointer = ctypes.cast(
		ctypes.pointer(ctypes.pointer(source_buffer)),
		ctypes.POINTER(ctypes.POINTER(ctypes.c_char)))

	# compile shader

	gl.glShaderSource(target, 1, buffer_pointer, ctypes.byref(source_length))
	gl.glCompileShader(target)

	# handle potential errors

	log_length = gl.GLint(0)
	gl.glGetShaderiv(target, gl.GL_INFO_LOG_LENGTH, ctypes.byref(log_length))

	log_buffer = ctypes.create_string_buffer(log_length.value)
	gl.glGetShaderInfoLog(target, log_length, None, log_buffer)

	if log_length.value > 1:
		raise Shader_error(str(log_buffer.value))

class Shader:
	def __init__(self, vert_path, frag_path):
		self.program = gl.glCreateProgram()

		# create vertex shader

		self.vert_shader = gl.glCreateShader(gl.GL_VERTEX_SHADER)
		create_shader(self.vert_shader, vert_path)
		gl.glAttachShader(self.program, self.vert_shader)

		# create fragment shader

		self.frag_shader = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
		create_shader(self.frag_shader, frag_path)
		gl.glAttachShader(self.program, self.frag_shader)

		# link program and clean up

		gl.glLinkProgram(self.program)

		gl.glDeleteShader(self.vert_shader)
		gl.glDeleteShader(self.frag_shader)

	def __del__(self):
		gl.glDeleteProgram(self.program)

	def find_uniform(self, name):
		return gl.glGetUniformLocation(self.program, ctypes.create_string_buffer(name))

	def uniform_matrix(self, location, matrix):
		gl.glUniformMatrix4fv(location, 1, gl.GL_FALSE, glm.value_ptr(matrix))

	def uniform_float(self, location, value):
		gl.glUniform1f(location, value)

	def use(self):
		gl.glUseProgram(self.program)

	def stop(self):
		gl.glUseProgram(0)
		#testcases
class ShaderTestCase(unittest.TestCase):
    def test_create_shader_success(self):
        # Test case for successful shader compilation
        target = gl.glCreateShader(gl.GL_VERTEX_SHADER)
        source_path = "path/to/vertex_shader.vert"
        
        with patch("builtins.open", mock_open(read_data="shader_source_code")) as mock_file:
            create_shader(target, source_path)
        
        gl.glCompileShader.assert_called_once_with(target)
        gl.glGetShaderiv.assert_called_once_with(target, gl.GL_INFO_LOG_LENGTH, ctypes.byref(gl.GLint()))
        gl.glGetShaderInfoLog.assert_not_called()

    def test_create_shader_error(self):
        # Test case for shader compilation error
        target = gl.glCreateShader(gl.GL_VERTEX_SHADER)
        source_path = "path/to/vertex_shader.vert"
        
        with patch("builtins.open", mock_open(read_data="shader_source_code")) as mock_file:
            gl.glGetShaderiv.return_value = 1  # Error log length > 1
            gl.glGetShaderInfoLog.return_value = b"Shader compilation error"
            with self.assertRaises(Shader_error) as cm:
                create_shader(target, source_path)
            self.assertEqual(str(cm.exception), "b'Shader compilation error'")

    def test_shader_init(self):
        # Test case for Shader class initialization
        vert_path = "path/to/vertex_shader.vert"
        frag_path = "path/to/fragment_shader.frag"
        
        with patch.object(gl, "glCreateProgram") as mock_create_program, \
                patch.object(gl, "glCreateShader") as mock_create_shader, \
                patch.object(gl, "glAttachShader") as mock_attach_shader, \
                patch.object(gl, "glLinkProgram") as mock_link_program, \
                patch.object(gl, "glDeleteShader") as mock_delete_shader:
            shader = Shader(vert_path, frag_path)
            
            mock_create_program.assert_called_once()
            
            mock_create_shader.assert_any_call(gl.GL_VERTEX_SHADER)
            mock_create_shader.assert_any_call(gl.GL_FRAGMENT_SHADER)
            
            mock_attach_shader.assert_any_call(shader.program, shader.vert_shader)
            mock_attach_shader.assert_any_call(shader.program, shader.frag_shader)
            
            mock_link_program.assert_called_with(shader.program)
            
            mock_delete_shader.assert_called_with(shader.vert_shader)
            mock_delete_shader.assert_called_with(shader.frag_shader)

    def test_shader_find_uniform(self):
        # Test case for finding a uniform location
        vert_path = "path/to/vertex_shader.vert"
        frag_path = "path/to/fragment_shader.frag"
        shader = Shader(vert_path, frag_path)
        uniform_name = "projectionMatrix"
        
        with patch.object(gl, "glGetUniformLocation") as mock_get_uniform_location:
            mock_get_uniform_location.return_value = 42
            location = shader.find_uniform(uniform_name)
            mock_get_uniform_location.assert_called_with(shader.program, ctypes.create_string_buffer(uniform_name.encode()))
            self.assertEqual(location, 42)

    def test_shader_uniform_matrix(self):
        # Test case for setting a matrix uniform
        vert_path = "path/to/vertex_shader.vert"
        frag_path = "path/to/fragment_shader.frag"
        shader = Shader(vert_path, frag_path)
        location = 42
        matrix = glm.mat4(1.0)
        
        with patch.object(gl, "glUniformMatrix4fv") as mock_uniform_matrix:
            shader.uniform_matrix(location, matrix)
            mock_uniform_matrix.assert_called_with(location, 1, gl.GL_FALSE, glm.value_ptr(matrix))

    def test_shader_uniform_float(self):
        # Test case for setting a float uniform
        vert_path = "path/to/vertex_shader.vert"
        frag_path = "path/to/fragment_shader.frag"
        shader = Shader(vert_path, frag_path)
        location = 42
        value = 3.14
        
        with patch.object(gl, "glUniform1f") as mock_uniform_float:
            shader.uniform_float(location, value)
            mock_uniform_float.assert_called_with(location, value)

    def test_shader_use(self):
        # Test case for using the shader program
        vert_path = "path/to/vertex_shader.vert"
        frag_path = "path/to/fragment_shader.frag"
        shader = Shader(vert_path, frag_path)
        
        with patch.object(gl, "glUseProgram") as mock_use_program:
            shader.use()
            mock_use_program.assert_called_with(shader.program)

    def test_shader_stop(self):
        # Test case for stopping the shader program
        vert_path = "path/to/vertex_shader.vert"
        frag_path = "path/to/fragment_shader.frag"
        shader = Shader(vert_path, frag_path)
        
        with patch.object(gl, "glUseProgram") as mock_use_program:
            shader.stop()
            mock_use_program.assert_called_with(0)


if __name__ == '__main__':
    unittest.main()


