from transformers import pipeline

classifier = pipeline("fill-mask")
classifier("Hello, <mask>!")