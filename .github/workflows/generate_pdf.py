import anthropic
import os
from datetime import datetime

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4000,
    messages=[
        {
            "role": "user",
            "content": "Genera un PDF con [AQUI DESCRIBES LO QUE QUIERES]. Proporciona el contenido en formato que pueda convertirse a PDF."
        }
    ]
)

# Guarda la respuesta
with open("output.txt", "w") as f:
    f.write(message.content[0].text)

print(f"PDF generado a las {datetime.now()}")
print("Contenido guardado en output.txt")
