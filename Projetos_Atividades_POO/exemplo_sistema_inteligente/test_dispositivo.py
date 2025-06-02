import unittest
from dispositivo import SensorTemperatura, AtuadorLuz

class TestDispositivoInteligente(unittest.TestCase):

    # Teste de comportamento esperado (polimorfismo)
    def test_sensor_operacao_ativo(self):
        sensor = SensorTemperatura("Sensor1", 30.5)
        sensor.ativar()
        resultado = sensor.operacao()
        self.assertEqual(resultado, "Sensor1 mede 30.5°C")

    # Teste de alteração de estado interno
    def test_atuador_muda_intensidade(self):
        luz = AtuadorLuz("LuzSala")
        luz.ativar()
        luz.ajustar_intensidade(75)
        self.assertEqual(luz.get_intensidade(), 75)

    # Teste de encapsulamento com setter (e controle de acesso ao valor)
    def test_set_intensidade_invalida(self):
        luz = AtuadorLuz("LuzQuarto")
        with self.assertRaises(ValueError):
            luz.ajustar_intensidade(150)  # Valor inválido

    # Teste de estado ativo (uso de método público)
    def test_sensor_estado_ativo(self):
        sensor = SensorTemperatura("Sensor2")
        self.assertFalse(sensor.esta_ativo())
        sensor.ativar()
        self.assertTrue(sensor.esta_ativo())

    # Teste de nome protegido com propriedade
    def test_nome_propriedade(self):
        sensor = SensorTemperatura("TempSensor")
        self.assertEqual(sensor.nome, "TempSensor")

if __name__ == "__main__":
    unittest.main()
