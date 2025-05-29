from deepseek_vl import DeepSeekVL

model = DeepSeekVL.from_pretrained()
image = load_image("room.jpg")
question = ""
answer = model.ask(image, question)