from PIL import Image, ImageFilter

# فتح الصورة
img = Image.open("input.jpg")

# تحويل لأبيض وأسود
gray = img.convert("L")

# تطبيق فلتر (توضيح الحواف)
filtered = gray.filter(ImageFilter.EDGE_ENHANCE)

# حفظ الصورة
filtered.save("output.jpg")

print("تمت المعالجة بنجاح ✅")
