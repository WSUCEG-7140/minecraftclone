"""
| This module implements issue#15 assigned to kruslin2 and passed automated unittest with 100% coverage
| The coverage report in pdf format is attached to the GitHub link pull request associated with issue#15.
| It declares all geometric variables needed to create spice up 3D block models for terrain
"""

#import module to write testcases for the code
import unittest

# constant variable initializations

# It is transparent, True or False
transparent = True

# it is cube, True or False
is_cube = False

# It is glass, True or False
glass = False

# It has no colliders values to initialize
colliders = []

# List initializations
bones = [{'name':'body','pivot':[0.0, 1.5, 0.0],'vertices':[[-0.25, 0.75, -0.125, -0.25, 1.5, -0.125, 0.25, 1.5, -0.125, 0.25, 0.75, -0.125], [0.25, 0.75, 0.125, 0.25, 1.5, 0.125, -0.25, 1.5, 0.125, -0.25, 0.75, 0.125], [-0.25, 1.5, -0.125, -0.25, 1.5, 0.125, 0.25, 1.5, 0.125, 0.25, 1.5, -0.125], [0.25, 0.75, -0.125, 0.25, 0.75, 0.125, -0.25, 0.75, 0.125, -0.25, 0.75, -0.125], [0.25, 0.75, -0.125, 0.25, 1.5, -0.125, 0.25, 1.5, 0.125, 0.25, 0.75, 0.125], [-0.25, 0.75, 0.125, -0.25, 1.5, 0.125, -0.25, 1.5, -0.125, -0.25, 0.75, -0.125]],'tex_coords':[[0.018867924528301886, 0.0, 0.018867924528301886, 0.75, 0.05660377358490566, 0.75, 0.05660377358490566, 0.0], [0.07547169811320754, 0.0, 0.07547169811320754, 0.75, 0.11320754716981132, 0.75, 0.11320754716981132, 0.0], [0.018867924528301886, 0.75, 0.018867924528301886, 1.0, 0.05660377358490566, 1.0, 0.05660377358490566, 0.75], [0.05660377358490566, 0.75, 0.05660377358490566, 1.0, 0.09433962264150944, 1.0, 0.09433962264150944, 0.75], [0.05660377358490566, 0.0, 0.05660377358490566, 0.75, 0.07547169811320754, 0.75, 0.07547169811320754, 0.0], [0.0, 0.0, 0.0, 0.75, 0.018867924528301886, 0.75, 0.018867924528301886, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'head','pivot':[0.0, 1.5, 0.0],'vertices':[[-0.2536456286907196, 1.497308611869812, -0.23161627352237701, -0.2536456286907196, 1.997308611869812, -0.23161627352237701, 0.2463543713092804, 1.997308611869812, -0.23161627352237701, 0.2463543713092804, 1.497308611869812, -0.23161627352237701], [0.2463543713092804, 1.497308611869812, 0.2683837413787842, 0.2463543713092804, 1.997308611869812, 0.2683837413787842, -0.2536456286907196, 1.997308611869812, 0.2683837413787842, -0.2536456286907196, 1.497308611869812, 0.2683837413787842], [-0.2536456286907196, 1.997308611869812, -0.23161627352237701, -0.2536456286907196, 1.997308611869812, 0.2683837413787842, 0.2463543713092804, 1.997308611869812, 0.2683837413787842, 0.2463543713092804, 1.997308611869812, -0.23161627352237701], [0.2463543713092804, 1.497308611869812, -0.23161627352237701, 0.2463543713092804, 1.497308611869812, 0.2683837413787842, -0.2536456286907196, 1.497308611869812, 0.2683837413787842, -0.2536456286907196, 1.497308611869812, -0.23161627352237701], [0.2463543713092804, 1.497308611869812, -0.23161627352237701, 0.2463543713092804, 1.997308611869812, -0.23161627352237701, 0.2463543713092804, 1.997308611869812, 0.2683837413787842, 0.2463543713092804, 1.497308611869812, 0.2683837413787842], [-0.2536456286907196, 1.497308611869812, 0.2683837413787842, -0.2536456286907196, 1.997308611869812, 0.2683837413787842, -0.2536456286907196, 1.997308611869812, -0.23161627352237701, -0.2536456286907196, 1.497308611869812, -0.23161627352237701], [0.2316092699766159, 0.8962944149971008, -0.21831698715686798, 0.2316092699766159, 1.396294355392456, -0.21831698715686798, 0.7316092848777771, 1.396294355392456, -0.21831698715686798, 0.7316092848777771, 0.8962944149971008, -0.21831698715686798], [0.7316092848777771, 0.8962944149971008, 0.2816829979419708, 0.7316092848777771, 1.396294355392456, 0.2816829979419708, 0.2316092699766159, 1.396294355392456, 0.2816829979419708, 0.2316092699766159, 0.8962944149971008, 0.2816829979419708], [0.2316092699766159, 1.396294355392456, -0.21831698715686798, 0.2316092699766159, 1.396294355392456, 0.2816829979419708, 0.7316092848777771, 1.396294355392456, 0.2816829979419708, 0.7316092848777771, 1.396294355392456, -0.21831698715686798], [0.7316092848777771, 0.8962944149971008, -0.21831698715686798, 0.7316092848777771, 0.8962944149971008, 0.2816829979419708, 0.2316092699766159, 0.8962944149971008, 0.2816829979419708, 0.2316092699766159, 0.8962944149971008, -0.21831698715686798], [0.7316092848777771, 0.8962944149971008, -0.21831698715686798, 0.7316092848777771, 1.396294355392456, -0.21831698715686798, 0.7316092848777771, 1.396294355392456, 0.2816829979419708, 0.7316092848777771, 0.8962944149971008, 0.2816829979419708], [0.2316092699766159, 0.8962944149971008, 0.2816829979419708, 0.2316092699766159, 1.396294355392456, 0.2816829979419708, 0.2316092699766159, 1.396294355392456, -0.21831698715686798, 0.2316092699766159, 0.8962944149971008, -0.21831698715686798]],'tex_coords':[[0.1509433962264151, 0.0, 0.1509433962264151, 0.5, 0.18867924528301888, 0.5, 0.18867924528301888, 0.0], [0.22641509433962265, 0.0, 0.22641509433962265, 0.5, 0.2641509433962264, 0.5, 0.2641509433962264, 0.0], [0.1509433962264151, 0.5, 0.1509433962264151, 1.0, 0.18867924528301888, 1.0, 0.18867924528301888, 0.5], [0.18867924528301888, 0.5, 0.18867924528301888, 1.0, 0.22641509433962265, 1.0, 0.22641509433962265, 0.5], [0.18867924528301888, 0.0, 0.18867924528301888, 0.5, 0.22641509433962265, 0.5, 0.22641509433962265, 0.0], [0.11320754716981132, 0.0, 0.11320754716981132, 0.5, 0.1509433962264151, 0.5, 0.1509433962264151, 0.0], [0.3018867924528302, 0.0, 0.3018867924528302, 0.5, 0.33962264150943394, 0.5, 0.33962264150943394, 0.0], [0.37735849056603776, 0.0, 0.37735849056603776, 0.5, 0.41509433962264153, 0.5, 0.41509433962264153, 0.0], [0.3018867924528302, 0.5, 0.3018867924528302, 1.0, 0.33962264150943394, 1.0, 0.33962264150943394, 0.5], [0.33962264150943394, 0.5, 0.33962264150943394, 1.0, 0.37735849056603776, 1.0, 0.37735849056603776, 0.5], [0.33962264150943394, 0.0, 0.33962264150943394, 0.5, 0.37735849056603776, 0.5, 0.37735849056603776, 0.0], [0.2641509433962264, 0.0, 0.2641509433962264, 0.5, 0.3018867924528302, 0.5, 0.3018867924528302, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'hat','pivot':[0.0, 1.5, 0.0],'vertices':[[-0.25, 1.5, -0.25, -0.25, 2.0, -0.25, 0.25, 2.0, -0.25, 0.25, 1.5, -0.25], [0.25, 1.5, 0.25, 0.25, 2.0, 0.25, -0.25, 2.0, 0.25, -0.25, 1.5, 0.25], [-0.25, 2.0, -0.25, -0.25, 2.0, 0.25, 0.25, 2.0, 0.25, 0.25, 2.0, -0.25], [0.25, 1.5, -0.25, 0.25, 1.5, 0.25, -0.25, 1.5, 0.25, -0.25, 1.5, -0.25], [0.25, 1.5, -0.25, 0.25, 2.0, -0.25, 0.25, 2.0, 0.25, 0.25, 1.5, 0.25], [-0.25, 1.5, 0.25, -0.25, 2.0, 0.25, -0.25, 2.0, -0.25, -0.25, 1.5, -0.25]],'tex_coords':[[0.4528301886792453, 0.0, 0.4528301886792453, 0.5, 0.49056603773584906, 0.5, 0.49056603773584906, 0.0], [0.5283018867924528, 0.0, 0.5283018867924528, 0.5, 0.5660377358490566, 0.5, 0.5660377358490566, 0.0], [0.4528301886792453, 0.5, 0.4528301886792453, 1.0, 0.49056603773584906, 1.0, 0.49056603773584906, 0.5], [0.49056603773584906, 0.5, 0.49056603773584906, 1.0, 0.5283018867924528, 1.0, 0.5283018867924528, 0.5], [0.49056603773584906, 0.0, 0.49056603773584906, 0.5, 0.5283018867924528, 0.5, 0.5283018867924528, 0.0], [0.41509433962264153, 0.0, 0.41509433962264153, 0.5, 0.4528301886792453, 0.5, 0.4528301886792453, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'rightArm','pivot':[-0.3125, 1.375, 0.0],'vertices':[[-0.5, 0.75, -0.125, -0.5, 1.5, -0.125, -0.25, 1.5, -0.125, -0.25, 0.75, -0.125], [-0.25, 0.75, 0.125, -0.25, 1.5, 0.125, -0.5, 1.5, 0.125, -0.5, 0.75, 0.125], [-0.5, 1.5, -0.125, -0.5, 1.5, 0.125, -0.25, 1.5, 0.125, -0.25, 1.5, -0.125], [-0.25, 0.75, -0.125, -0.25, 0.75, 0.125, -0.5, 0.75, 0.125, -0.5, 0.75, -0.125], [-0.25, 0.75, -0.125, -0.25, 1.5, -0.125, -0.25, 1.5, 0.125, -0.25, 0.75, 0.125], [-0.5, 0.75, 0.125, -0.5, 1.5, 0.125, -0.5, 1.5, -0.125, -0.5, 0.75, -0.125]],'tex_coords':[[0.5849056603773585, 0.0, 0.5849056603773585, 0.75, 0.6037735849056604, 0.75, 0.6037735849056604, 0.0], [0.6226415094339622, 0.0, 0.6226415094339622, 0.75, 0.6415094339622641, 0.75, 0.6415094339622641, 0.0], [0.5849056603773585, 0.75, 0.5849056603773585, 1.0, 0.6037735849056604, 1.0, 0.6037735849056604, 0.75], [0.6037735849056604, 0.75, 0.6037735849056604, 1.0, 0.6226415094339622, 1.0, 0.6226415094339622, 0.75], [0.6037735849056604, 0.0, 0.6037735849056604, 0.75, 0.6226415094339622, 0.75, 0.6226415094339622, 0.0], [0.5660377358490566, 0.0, 0.5660377358490566, 0.75, 0.5849056603773585, 0.75, 0.5849056603773585, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'leftArm','pivot':[0.3125, 1.375, 0.0],'vertices':[[0.7019792795181274, 0.748781681060791, -0.02643335424363613, 0.7019792795181274, 1.498781681060791, -0.02643335424363613, 0.9519792795181274, 1.498781681060791, -0.02643335424363613, 0.9519792795181274, 0.748781681060791, -0.02643335424363613], [0.9519792795181274, 0.748781681060791, 0.22356665134429932, 0.9519792795181274, 1.498781681060791, 0.22356665134429932, 0.7019792795181274, 1.498781681060791, 0.22356665134429932, 0.7019792795181274, 0.748781681060791, 0.22356665134429932], [0.7019792795181274, 1.498781681060791, -0.02643335424363613, 0.7019792795181274, 1.498781681060791, 0.22356665134429932, 0.9519792795181274, 1.498781681060791, 0.22356665134429932, 0.9519792795181274, 1.498781681060791, -0.02643335424363613], [0.9519792795181274, 0.748781681060791, -0.02643335424363613, 0.9519792795181274, 0.748781681060791, 0.22356665134429932, 0.7019792795181274, 0.748781681060791, 0.22356665134429932, 0.7019792795181274, 0.748781681060791, -0.02643335424363613], [0.9519792795181274, 0.748781681060791, -0.02643335424363613, 0.9519792795181274, 1.498781681060791, -0.02643335424363613, 0.9519792795181274, 1.498781681060791, 0.22356665134429932, 0.9519792795181274, 0.748781681060791, 0.22356665134429932], [0.7019792795181274, 0.748781681060791, 0.22356665134429932, 0.7019792795181274, 1.498781681060791, 0.22356665134429932, 0.7019792795181274, 1.498781681060791, -0.02643335424363613, 0.7019792795181274, 0.748781681060791, -0.02643335424363613], [0.09342791140079498, 1.3167552947998047, -0.06984145194292068, 0.09342791140079498, 1.5042552947998047, -0.06984145194292068, 0.7184278964996338, 1.5042552947998047, -0.06984145194292068, 0.7184278964996338, 1.3167552947998047, -0.06984145194292068], [0.7184278964996338, 1.3167552947998047, 0.18015854060649872, 0.7184278964996338, 1.5042552947998047, 0.18015854060649872, 0.09342791140079498, 1.5042552947998047, 0.18015854060649872, 0.09342791140079498, 1.3167552947998047, 0.18015854060649872], [0.09342791140079498, 1.5042552947998047, -0.06984145194292068, 0.09342791140079498, 1.5042552947998047, 0.18015854060649872, 0.7184278964996338, 1.5042552947998047, 0.18015854060649872, 0.7184278964996338, 1.5042552947998047, -0.06984145194292068], [0.7184278964996338, 1.3167552947998047, -0.06984145194292068, 0.7184278964996338, 1.3167552947998047, 0.18015854060649872, 0.09342791140079498, 1.3167552947998047, 0.18015854060649872, 0.09342791140079498, 1.3167552947998047, -0.06984145194292068], [0.7184278964996338, 1.3167552947998047, -0.06984145194292068, 0.7184278964996338, 1.5042552947998047, -0.06984145194292068, 0.7184278964996338, 1.5042552947998047, 0.18015854060649872, 0.7184278964996338, 1.3167552947998047, 0.18015854060649872], [0.09342791140079498, 1.3167552947998047, 0.18015854060649872, 0.09342791140079498, 1.5042552947998047, 0.18015854060649872, 0.09342791140079498, 1.5042552947998047, -0.06984145194292068, 0.09342791140079498, 1.3167552947998047, -0.06984145194292068]],'tex_coords':[[0.660377358490566, 0.0, 0.660377358490566, 0.75, 0.6792452830188679, 0.75, 0.6792452830188679, 0.0], [0.6981132075471698, 0.0, 0.6981132075471698, 0.75, 0.7169811320754716, 0.75, 0.7169811320754716, 0.0], [0.660377358490566, 0.75, 0.660377358490566, 1.0, 0.6792452830188679, 1.0, 0.6792452830188679, 0.75], [0.6792452830188679, 0.75, 0.6792452830188679, 1.0, 0.6981132075471698, 1.0, 0.6981132075471698, 0.75], [0.6792452830188679, 0.0, 0.6792452830188679, 0.75, 0.6981132075471698, 0.75, 0.6981132075471698, 0.0], [0.6415094339622641, 0.0, 0.6415094339622641, 0.75, 0.660377358490566, 0.75, 0.660377358490566, 0.0], [0.7358490566037735, 0.5625, 0.7358490566037735, 0.75, 0.7830188679245284, 0.75, 0.7830188679245284, 0.5625], [0.8018867924528302, 0.5625, 0.8018867924528302, 0.75, 0.8490566037735849, 0.75, 0.8490566037735849, 0.5625], [0.7358490566037735, 0.75, 0.7358490566037735, 1.0, 0.7830188679245284, 1.0, 0.7830188679245284, 0.75], [0.7830188679245284, 0.75, 0.7830188679245284, 1.0, 0.8301886792452831, 1.0, 0.8301886792452831, 0.75], [0.7830188679245284, 0.5625, 0.7830188679245284, 0.75, 0.8018867924528302, 0.75, 0.8018867924528302, 0.5625], [0.7169811320754716, 0.5625, 0.7169811320754716, 0.75, 0.7358490566037735, 0.75, 0.7358490566037735, 0.5625]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'rightLeg','pivot':[-0.11875, 0.75, 0.0],'vertices':[[-0.24375000596046448, 0.0, -0.125, -0.24375000596046448, 0.75, -0.125, 0.0062500000931322575, 0.75, -0.125, 0.0062500000931322575, 0.0, -0.125], [0.0062500000931322575, 0.0, 0.125, 0.0062500000931322575, 0.75, 0.125, -0.24375000596046448, 0.75, 0.125, -0.24375000596046448, 0.0, 0.125], [-0.24375000596046448, 0.75, -0.125, -0.24375000596046448, 0.75, 0.125, 0.0062500000931322575, 0.75, 0.125, 0.0062500000931322575, 0.75, -0.125], [0.0062500000931322575, 0.0, -0.125, 0.0062500000931322575, 0.0, 0.125, -0.24375000596046448, 0.0, 0.125, -0.24375000596046448, 0.0, -0.125], [0.0062500000931322575, 0.0, -0.125, 0.0062500000931322575, 0.75, -0.125, 0.0062500000931322575, 0.75, 0.125, 0.0062500000931322575, 0.0, 0.125], [-0.24375000596046448, 0.0, 0.125, -0.24375000596046448, 0.75, 0.125, -0.24375000596046448, 0.75, -0.125, -0.24375000596046448, 0.0, -0.125]],'tex_coords':[[0.8679245283018868, 0.0, 0.8679245283018868, 0.75, 0.8867924528301887, 0.75, 0.8867924528301887, 0.0], [0.9056603773584906, 0.0, 0.9056603773584906, 0.75, 0.9245283018867925, 0.75, 0.9245283018867925, 0.0], [0.8679245283018868, 0.75, 0.8679245283018868, 1.0, 0.8867924528301887, 1.0, 0.8867924528301887, 0.75], [0.8867924528301887, 0.75, 0.8867924528301887, 1.0, 0.9056603773584906, 1.0, 0.9056603773584906, 0.75], [0.8867924528301887, 0.0, 0.8867924528301887, 0.75, 0.9056603773584906, 0.75, 0.9056603773584906, 0.0], [0.8490566037735849, 0.0, 0.8490566037735849, 0.75, 0.8679245283018868, 0.75, 0.8679245283018868, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'leftLeg','pivot':[0.11875, 0.75, 0.0],'vertices':[[-0.0062500000931322575, 0.0, -0.125, -0.0062500000931322575, 0.75, -0.125, 0.24375000596046448, 0.75, -0.125, 0.24375000596046448, 0.0, -0.125], [0.24375000596046448, 0.0, 0.125, 0.24375000596046448, 0.75, 0.125, -0.0062500000931322575, 0.75, 0.125, -0.0062500000931322575, 0.0, 0.125], [-0.0062500000931322575, 0.75, -0.125, -0.0062500000931322575, 0.75, 0.125, 0.24375000596046448, 0.75, 0.125, 0.24375000596046448, 0.75, -0.125], [0.24375000596046448, 0.0, -0.125, 0.24375000596046448, 0.0, 0.125, -0.0062500000931322575, 0.0, 0.125, -0.0062500000931322575, 0.0, -0.125], [0.24375000596046448, 0.0, -0.125, 0.24375000596046448, 0.75, -0.125, 0.24375000596046448, 0.75, 0.125, 0.24375000596046448, 0.0, 0.125], [-0.0062500000931322575, 0.0, 0.125, -0.0062500000931322575, 0.75, 0.125, -0.0062500000931322575, 0.75, -0.125, -0.0062500000931322575, 0.0, -0.125]],'tex_coords':[[0.9433962264150944, 0.0, 0.9433962264150944, 0.75, 0.9622641509433962, 0.75, 0.9622641509433962, 0.0], [0.9811320754716981, 0.0, 0.9811320754716981, 0.75, 1.0, 0.75, 1.0, 0.0], [0.9433962264150944, 0.75, 0.9433962264150944, 1.0, 0.9622641509433962, 1.0, 0.9622641509433962, 0.75], [0.9622641509433962, 0.75, 0.9622641509433962, 1.0, 0.9811320754716981, 1.0, 0.9811320754716981, 0.75], [0.9622641509433962, 0.0, 0.9622641509433962, 0.75, 0.9811320754716981, 0.75, 0.9811320754716981, 0.0], [0.9245283018867925, 0.0, 0.9245283018867925, 0.75, 0.9433962264150944, 0.75, 0.9433962264150944, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}]

# Class Unittest
class MyCodeTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary test data or configurations

        # Initialize the code variables for testing
        self.transparent = True
        self.is_cube = False
        self.glass = False
        self.colliders = []

        self.bones = [{'name':'body','pivot':[0.0, 1.5, 0.0],'vertices':[[-0.25, 0.75, -0.125, -0.25, 1.5, -0.125, 0.25, 1.5, -0.125, 0.25, 0.75, -0.125], [0.25, 0.75, 0.125, 0.25, 1.5, 0.125, -0.25, 1.5, 0.125, -0.25, 0.75, 0.125], [-0.25, 1.5, -0.125, -0.25, 1.5, 0.125, 0.25, 1.5, 0.125, 0.25, 1.5, -0.125], [0.25, 0.75, -0.125, 0.25, 0.75, 0.125, -0.25, 0.75, 0.125, -0.25, 0.75, -0.125], [0.25, 0.75, -0.125, 0.25, 1.5, -0.125, 0.25, 1.5, 0.125, 0.25, 0.75, 0.125], [-0.25, 0.75, 0.125, -0.25, 1.5, 0.125, -0.25, 1.5, -0.125, -0.25, 0.75, -0.125]],'tex_coords':[[0.018867924528301886, 0.0, 0.018867924528301886, 0.75, 0.05660377358490566, 0.75, 0.05660377358490566, 0.0], [0.07547169811320754, 0.0, 0.07547169811320754, 0.75, 0.11320754716981132, 0.75, 0.11320754716981132, 0.0], [0.018867924528301886, 0.75, 0.018867924528301886, 1.0, 0.05660377358490566, 1.0, 0.05660377358490566, 0.75], [0.05660377358490566, 0.75, 0.05660377358490566, 1.0, 0.09433962264150944, 1.0, 0.09433962264150944, 0.75], [0.05660377358490566, 0.0, 0.05660377358490566, 0.75, 0.07547169811320754, 0.75, 0.07547169811320754, 0.0], [0.0, 0.0, 0.0, 0.75, 0.018867924528301886, 0.75, 0.018867924528301886, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'head','pivot':[0.0, 1.5, 0.0],'vertices':[[-0.2536456286907196, 1.497308611869812, -0.23161627352237701, -0.2536456286907196, 1.997308611869812, -0.23161627352237701, 0.2463543713092804, 1.997308611869812, -0.23161627352237701, 0.2463543713092804, 1.497308611869812, -0.23161627352237701], [0.2463543713092804, 1.497308611869812, 0.2683837413787842, 0.2463543713092804, 1.997308611869812, 0.2683837413787842, -0.2536456286907196, 1.997308611869812, 0.2683837413787842, -0.2536456286907196, 1.497308611869812, 0.2683837413787842], [-0.2536456286907196, 1.997308611869812, -0.23161627352237701, -0.2536456286907196, 1.997308611869812, 0.2683837413787842, 0.2463543713092804, 1.997308611869812, 0.2683837413787842, 0.2463543713092804, 1.997308611869812, -0.23161627352237701], [0.2463543713092804, 1.497308611869812, -0.23161627352237701, 0.2463543713092804, 1.497308611869812, 0.2683837413787842, -0.2536456286907196, 1.497308611869812, 0.2683837413787842, -0.2536456286907196, 1.497308611869812, -0.23161627352237701], [0.2463543713092804, 1.497308611869812, -0.23161627352237701, 0.2463543713092804, 1.997308611869812, -0.23161627352237701, 0.2463543713092804, 1.997308611869812, 0.2683837413787842, 0.2463543713092804, 1.497308611869812, 0.2683837413787842], [-0.2536456286907196, 1.497308611869812, 0.2683837413787842, -0.2536456286907196, 1.997308611869812, 0.2683837413787842, -0.2536456286907196, 1.997308611869812, -0.23161627352237701, -0.2536456286907196, 1.497308611869812, -0.23161627352237701], [0.2316092699766159, 0.8962944149971008, -0.21831698715686798, 0.2316092699766159, 1.396294355392456, -0.21831698715686798, 0.7316092848777771, 1.396294355392456, -0.21831698715686798, 0.7316092848777771, 0.8962944149971008, -0.21831698715686798], [0.7316092848777771, 0.8962944149971008, 0.2816829979419708, 0.7316092848777771, 1.396294355392456, 0.2816829979419708, 0.2316092699766159, 1.396294355392456, 0.2816829979419708, 0.2316092699766159, 0.8962944149971008, 0.2816829979419708], [0.2316092699766159, 1.396294355392456, -0.21831698715686798, 0.2316092699766159, 1.396294355392456, 0.2816829979419708, 0.7316092848777771, 1.396294355392456, 0.2816829979419708, 0.7316092848777771, 1.396294355392456, -0.21831698715686798], [0.7316092848777771, 0.8962944149971008, -0.21831698715686798, 0.7316092848777771, 0.8962944149971008, 0.2816829979419708, 0.2316092699766159, 0.8962944149971008, 0.2816829979419708, 0.2316092699766159, 0.8962944149971008, -0.21831698715686798], [0.7316092848777771, 0.8962944149971008, -0.21831698715686798, 0.7316092848777771, 1.396294355392456, -0.21831698715686798, 0.7316092848777771, 1.396294355392456, 0.2816829979419708, 0.7316092848777771, 0.8962944149971008, 0.2816829979419708], [0.2316092699766159, 0.8962944149971008, 0.2816829979419708, 0.2316092699766159, 1.396294355392456, 0.2816829979419708, 0.2316092699766159, 1.396294355392456, -0.21831698715686798, 0.2316092699766159, 0.8962944149971008, -0.21831698715686798]],'tex_coords':[[0.1509433962264151, 0.0, 0.1509433962264151, 0.5, 0.18867924528301888, 0.5, 0.18867924528301888, 0.0], [0.22641509433962265, 0.0, 0.22641509433962265, 0.5, 0.2641509433962264, 0.5, 0.2641509433962264, 0.0], [0.1509433962264151, 0.5, 0.1509433962264151, 1.0, 0.18867924528301888, 1.0, 0.18867924528301888, 0.5], [0.18867924528301888, 0.5, 0.18867924528301888, 1.0, 0.22641509433962265, 1.0, 0.22641509433962265, 0.5], [0.18867924528301888, 0.0, 0.18867924528301888, 0.5, 0.22641509433962265, 0.5, 0.22641509433962265, 0.0], [0.11320754716981132, 0.0, 0.11320754716981132, 0.5, 0.1509433962264151, 0.5, 0.1509433962264151, 0.0], [0.3018867924528302, 0.0, 0.3018867924528302, 0.5, 0.33962264150943394, 0.5, 0.33962264150943394, 0.0], [0.37735849056603776, 0.0, 0.37735849056603776, 0.5, 0.41509433962264153, 0.5, 0.41509433962264153, 0.0], [0.3018867924528302, 0.5, 0.3018867924528302, 1.0, 0.33962264150943394, 1.0, 0.33962264150943394, 0.5], [0.33962264150943394, 0.5, 0.33962264150943394, 1.0, 0.37735849056603776, 1.0, 0.37735849056603776, 0.5], [0.33962264150943394, 0.0, 0.33962264150943394, 0.5, 0.37735849056603776, 0.5, 0.37735849056603776, 0.0], [0.2641509433962264, 0.0, 0.2641509433962264, 0.5, 0.3018867924528302, 0.5, 0.3018867924528302, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'hat','pivot':[0.0, 1.5, 0.0],'vertices':[[-0.25, 1.5, -0.25, -0.25, 2.0, -0.25, 0.25, 2.0, -0.25, 0.25, 1.5, -0.25], [0.25, 1.5, 0.25, 0.25, 2.0, 0.25, -0.25, 2.0, 0.25, -0.25, 1.5, 0.25], [-0.25, 2.0, -0.25, -0.25, 2.0, 0.25, 0.25, 2.0, 0.25, 0.25, 2.0, -0.25], [0.25, 1.5, -0.25, 0.25, 1.5, 0.25, -0.25, 1.5, 0.25, -0.25, 1.5, -0.25], [0.25, 1.5, -0.25, 0.25, 2.0, -0.25, 0.25, 2.0, 0.25, 0.25, 1.5, 0.25], [-0.25, 1.5, 0.25, -0.25, 2.0, 0.25, -0.25, 2.0, -0.25, -0.25, 1.5, -0.25]],'tex_coords':[[0.4528301886792453, 0.0, 0.4528301886792453, 0.5, 0.49056603773584906, 0.5, 0.49056603773584906, 0.0], [0.5283018867924528, 0.0, 0.5283018867924528, 0.5, 0.5660377358490566, 0.5, 0.5660377358490566, 0.0], [0.4528301886792453, 0.5, 0.4528301886792453, 1.0, 0.49056603773584906, 1.0, 0.49056603773584906, 0.5], [0.49056603773584906, 0.5, 0.49056603773584906, 1.0, 0.5283018867924528, 1.0, 0.5283018867924528, 0.5], [0.49056603773584906, 0.0, 0.49056603773584906, 0.5, 0.5283018867924528, 0.5, 0.5283018867924528, 0.0], [0.41509433962264153, 0.0, 0.41509433962264153, 0.5, 0.4528301886792453, 0.5, 0.4528301886792453, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'rightArm','pivot':[-0.3125, 1.375, 0.0],'vertices':[[-0.5, 0.75, -0.125, -0.5, 1.5, -0.125, -0.25, 1.5, -0.125, -0.25, 0.75, -0.125], [-0.25, 0.75, 0.125, -0.25, 1.5, 0.125, -0.5, 1.5, 0.125, -0.5, 0.75, 0.125], [-0.5, 1.5, -0.125, -0.5, 1.5, 0.125, -0.25, 1.5, 0.125, -0.25, 1.5, -0.125], [-0.25, 0.75, -0.125, -0.25, 0.75, 0.125, -0.5, 0.75, 0.125, -0.5, 0.75, -0.125], [-0.25, 0.75, -0.125, -0.25, 1.5, -0.125, -0.25, 1.5, 0.125, -0.25, 0.75, 0.125], [-0.5, 0.75, 0.125, -0.5, 1.5, 0.125, -0.5, 1.5, -0.125, -0.5, 0.75, -0.125]],'tex_coords':[[0.5849056603773585, 0.0, 0.5849056603773585, 0.75, 0.6037735849056604, 0.75, 0.6037735849056604, 0.0], [0.6226415094339622, 0.0, 0.6226415094339622, 0.75, 0.6415094339622641, 0.75, 0.6415094339622641, 0.0], [0.5849056603773585, 0.75, 0.5849056603773585, 1.0, 0.6037735849056604, 1.0, 0.6037735849056604, 0.75], [0.6037735849056604, 0.75, 0.6037735849056604, 1.0, 0.6226415094339622, 1.0, 0.6226415094339622, 0.75], [0.6037735849056604, 0.0, 0.6037735849056604, 0.75, 0.6226415094339622, 0.75, 0.6226415094339622, 0.0], [0.5660377358490566, 0.0, 0.5660377358490566, 0.75, 0.5849056603773585, 0.75, 0.5849056603773585, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'leftArm','pivot':[0.3125, 1.375, 0.0],'vertices':[[0.7019792795181274, 0.748781681060791, -0.02643335424363613, 0.7019792795181274, 1.498781681060791, -0.02643335424363613, 0.9519792795181274, 1.498781681060791, -0.02643335424363613, 0.9519792795181274, 0.748781681060791, -0.02643335424363613], [0.9519792795181274, 0.748781681060791, 0.22356665134429932, 0.9519792795181274, 1.498781681060791, 0.22356665134429932, 0.7019792795181274, 1.498781681060791, 0.22356665134429932, 0.7019792795181274, 0.748781681060791, 0.22356665134429932], [0.7019792795181274, 1.498781681060791, -0.02643335424363613, 0.7019792795181274, 1.498781681060791, 0.22356665134429932, 0.9519792795181274, 1.498781681060791, 0.22356665134429932, 0.9519792795181274, 1.498781681060791, -0.02643335424363613], [0.9519792795181274, 0.748781681060791, -0.02643335424363613, 0.9519792795181274, 0.748781681060791, 0.22356665134429932, 0.7019792795181274, 0.748781681060791, 0.22356665134429932, 0.7019792795181274, 0.748781681060791, -0.02643335424363613], [0.9519792795181274, 0.748781681060791, -0.02643335424363613, 0.9519792795181274, 1.498781681060791, -0.02643335424363613, 0.9519792795181274, 1.498781681060791, 0.22356665134429932, 0.9519792795181274, 0.748781681060791, 0.22356665134429932], [0.7019792795181274, 0.748781681060791, 0.22356665134429932, 0.7019792795181274, 1.498781681060791, 0.22356665134429932, 0.7019792795181274, 1.498781681060791, -0.02643335424363613, 0.7019792795181274, 0.748781681060791, -0.02643335424363613], [0.09342791140079498, 1.3167552947998047, -0.06984145194292068, 0.09342791140079498, 1.5042552947998047, -0.06984145194292068, 0.7184278964996338, 1.5042552947998047, -0.06984145194292068, 0.7184278964996338, 1.3167552947998047, -0.06984145194292068], [0.7184278964996338, 1.3167552947998047, 0.18015854060649872, 0.7184278964996338, 1.5042552947998047, 0.18015854060649872, 0.09342791140079498, 1.5042552947998047, 0.18015854060649872, 0.09342791140079498, 1.3167552947998047, 0.18015854060649872], [0.09342791140079498, 1.5042552947998047, -0.06984145194292068, 0.09342791140079498, 1.5042552947998047, 0.18015854060649872, 0.7184278964996338, 1.5042552947998047, 0.18015854060649872, 0.7184278964996338, 1.5042552947998047, -0.06984145194292068], [0.7184278964996338, 1.3167552947998047, -0.06984145194292068, 0.7184278964996338, 1.3167552947998047, 0.18015854060649872, 0.09342791140079498, 1.3167552947998047, 0.18015854060649872, 0.09342791140079498, 1.3167552947998047, -0.06984145194292068], [0.7184278964996338, 1.3167552947998047, -0.06984145194292068, 0.7184278964996338, 1.5042552947998047, -0.06984145194292068, 0.7184278964996338, 1.5042552947998047, 0.18015854060649872, 0.7184278964996338, 1.3167552947998047, 0.18015854060649872], [0.09342791140079498, 1.3167552947998047, 0.18015854060649872, 0.09342791140079498, 1.5042552947998047, 0.18015854060649872, 0.09342791140079498, 1.5042552947998047, -0.06984145194292068, 0.09342791140079498, 1.3167552947998047, -0.06984145194292068]],'tex_coords':[[0.660377358490566, 0.0, 0.660377358490566, 0.75, 0.6792452830188679, 0.75, 0.6792452830188679, 0.0], [0.6981132075471698, 0.0, 0.6981132075471698, 0.75, 0.7169811320754716, 0.75, 0.7169811320754716, 0.0], [0.660377358490566, 0.75, 0.660377358490566, 1.0, 0.6792452830188679, 1.0, 0.6792452830188679, 0.75], [0.6792452830188679, 0.75, 0.6792452830188679, 1.0, 0.6981132075471698, 1.0, 0.6981132075471698, 0.75], [0.6792452830188679, 0.0, 0.6792452830188679, 0.75, 0.6981132075471698, 0.75, 0.6981132075471698, 0.0], [0.6415094339622641, 0.0, 0.6415094339622641, 0.75, 0.660377358490566, 0.75, 0.660377358490566, 0.0], [0.7358490566037735, 0.5625, 0.7358490566037735, 0.75, 0.7830188679245284, 0.75, 0.7830188679245284, 0.5625], [0.8018867924528302, 0.5625, 0.8018867924528302, 0.75, 0.8490566037735849, 0.75, 0.8490566037735849, 0.5625], [0.7358490566037735, 0.75, 0.7358490566037735, 1.0, 0.7830188679245284, 1.0, 0.7830188679245284, 0.75], [0.7830188679245284, 0.75, 0.7830188679245284, 1.0, 0.8301886792452831, 1.0, 0.8301886792452831, 0.75], [0.7830188679245284, 0.5625, 0.7830188679245284, 0.75, 0.8018867924528302, 0.75, 0.8018867924528302, 0.5625], [0.7169811320754716, 0.5625, 0.7169811320754716, 0.75, 0.7358490566037735, 0.75, 0.7358490566037735, 0.5625]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'rightLeg','pivot':[-0.11875, 0.75, 0.0],'vertices':[[-0.24375000596046448, 0.0, -0.125, -0.24375000596046448, 0.75, -0.125, 0.0062500000931322575, 0.75, -0.125, 0.0062500000931322575, 0.0, -0.125], [0.0062500000931322575, 0.0, 0.125, 0.0062500000931322575, 0.75, 0.125, -0.24375000596046448, 0.75, 0.125, -0.24375000596046448, 0.0, 0.125], [-0.24375000596046448, 0.75, -0.125, -0.24375000596046448, 0.75, 0.125, 0.0062500000931322575, 0.75, 0.125, 0.0062500000931322575, 0.75, -0.125], [0.0062500000931322575, 0.0, -0.125, 0.0062500000931322575, 0.0, 0.125, -0.24375000596046448, 0.0, 0.125, -0.24375000596046448, 0.0, -0.125], [0.0062500000931322575, 0.0, -0.125, 0.0062500000931322575, 0.75, -0.125, 0.0062500000931322575, 0.75, 0.125, 0.0062500000931322575, 0.0, 0.125], [-0.24375000596046448, 0.0, 0.125, -0.24375000596046448, 0.75, 0.125, -0.24375000596046448, 0.75, -0.125, -0.24375000596046448, 0.0, -0.125]],'tex_coords':[[0.8679245283018868, 0.0, 0.8679245283018868, 0.75, 0.8867924528301887, 0.75, 0.8867924528301887, 0.0], [0.9056603773584906, 0.0, 0.9056603773584906, 0.75, 0.9245283018867925, 0.75, 0.9245283018867925, 0.0], [0.8679245283018868, 0.75, 0.8679245283018868, 1.0, 0.8867924528301887, 1.0, 0.8867924528301887, 0.75], [0.8867924528301887, 0.75, 0.8867924528301887, 1.0, 0.9056603773584906, 1.0, 0.9056603773584906, 0.75], [0.8867924528301887, 0.0, 0.8867924528301887, 0.75, 0.9056603773584906, 0.75, 0.9056603773584906, 0.0], [0.8490566037735849, 0.0, 0.8490566037735849, 0.75, 0.8679245283018868, 0.75, 0.8679245283018868, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'leftLeg','pivot':[0.11875, 0.75, 0.0],'vertices':[[-0.0062500000931322575, 0.0, -0.125, -0.0062500000931322575, 0.75, -0.125, 0.24375000596046448, 0.75, -0.125, 0.24375000596046448, 0.0, -0.125], [0.24375000596046448, 0.0, 0.125, 0.24375000596046448, 0.75, 0.125, -0.0062500000931322575, 0.75, 0.125, -0.0062500000931322575, 0.0, 0.125], [-0.0062500000931322575, 0.75, -0.125, -0.0062500000931322575, 0.75, 0.125, 0.24375000596046448, 0.75, 0.125, 0.24375000596046448, 0.75, -0.125], [0.24375000596046448, 0.0, -0.125, 0.24375000596046448, 0.0, 0.125, -0.0062500000931322575, 0.0, 0.125, -0.0062500000931322575, 0.0, -0.125], [0.24375000596046448, 0.0, -0.125, 0.24375000596046448, 0.75, -0.125, 0.24375000596046448, 0.75, 0.125, 0.24375000596046448, 0.0, 0.125], [-0.0062500000931322575, 0.0, 0.125, -0.0062500000931322575, 0.75, 0.125, -0.0062500000931322575, 0.75, -0.125, -0.0062500000931322575, 0.0, -0.125]],'tex_coords':[[0.9433962264150944, 0.0, 0.9433962264150944, 0.75, 0.9622641509433962, 0.75, 0.9622641509433962, 0.0], [0.9811320754716981, 0.0, 0.9811320754716981, 0.75, 1.0, 0.75, 1.0, 0.0], [0.9433962264150944, 0.75, 0.9433962264150944, 1.0, 0.9622641509433962, 1.0, 0.9622641509433962, 0.75], [0.9622641509433962, 0.75, 0.9622641509433962, 1.0, 0.9811320754716981, 1.0, 0.9811320754716981, 0.75], [0.9622641509433962, 0.0, 0.9622641509433962, 0.75, 0.9811320754716981, 0.75, 0.9811320754716981, 0.0], [0.9245283018867925, 0.0, 0.9245283018867925, 0.75, 0.9433962264150944, 0.75, 0.9433962264150944, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}]
    # test variable transparent
    def test_transparent(self):
        self.assertTrue(self.transparent)
    # test variable is_cube
    def test_is_cube(self):
        self.assertFalse(self.is_cube)
    # test variable glass
    def test_glass(self):
        self.assertFalse(self.glass)
    # test colliders variable
    def test_colliders(self):
        self.assertIsInstance(self.colliders, list)
    # test bones variable
    def test_bones(self):
        self.assertIsInstance(self.bones, list)


if __name__ == '__main__':
    unittest.main()
