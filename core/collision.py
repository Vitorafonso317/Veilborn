"""
Sistema simples para definir altura do chão para animações
"""

class CollisionManager:
    def __init__(self):
        # Apenas uma linha de chão simples para cada cenário
        self.ground_y = 500  # altura do chão padrão
        self.load_scenario("default")
        
    def load_scenario(self, scenario_name):
        """Define a altura do chão para cada cenário"""
        ground_heights = {
            "default": 500,    # chão a 500px do topo
            "forest": 450,     # chão da floresta mais alto
            "castle": 520,     # chão do castelo mais baixo
            "beach": 480,      # praia
            "mountain": 400    # montanha
        }
        
        self.ground_y = ground_heights.get(scenario_name, 500)
        
    def get_ground_height(self):
        """Retorna a altura do chão atual"""
        return self.ground_y
        
    def set_ground_height(self, height):
        """Define manualmente a altura do chão"""
        self.ground_y = height
        
    def is_on_ground(self, character_y, character_height):
        """Verifica se o personagem está no chão (para animações)"""
        return character_y + character_height >= self.ground_y