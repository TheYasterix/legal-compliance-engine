"""
Ejemplo técnico de uso del ComplianceEngine para análisis normativo.

Este archivo demuestra cómo podría utilizarse el motor jurídico
para procesar un texto legal y obtener una estructura inicial de análisis.
"""

from src.core import ComplianceEngine

engine = ComplianceEngine()

texto_legal = """
Artículo 7. Los servidores públicos deberán implementar mecanismos de control interno
para garantizar la correcta administración de recursos y el cumplimiento de obligaciones.
"""

resultado = engine.analyze_norm(texto_legal)

print("Resultado del análisis normativo:")
print(resultado)
