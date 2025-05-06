# -------------------------
# -- Book Library System --
# -------------------------

"""
📚  تطبيق ادارة مكتبة الكتب
1- إضافة كتاب جديد
2- عرض جميع الكتب
3- البحث عن كتاب بالاسم
4- حذف كتاب
5- حفظ الكتب في ملف نصي
6- خروج من التطبيق
"""

books = {}

def add_book():
    """إضافة كتاب جديد"""
    print("إضافة كتاب جديد")
    title = input("أدخل عنوان الكتاب: ").strip()
    author = input("أدخل اسم المؤلف: ").strip().capitalize()
    year = input("أدخل سنة النشر: ").strip()
    if not year.isdigit():
        print("سنة النشر يجب ان تكون رقم صحيح, مثال: 2025")
        return
    if title in books:
        print("هذا الكتاب موجود بالفعل")
        return
    if not title or not author or not year:
        print("يجب ملئ جميع الحقول")
        return
    else:
        books[title] = {
            "author" : author,
            "year" : year
        }
        print(f"تم إضافة الكتاب: {title} بنجاح")
    print(books)

def view_books():
    """عرض جميع الكتب"""
    print("عرض جميع الكتب")
    if not books:
        print("لا توجد كتب في المكتبة")
        return
    else:
        print(f"عدد الكتب في المكتبة: {len(books)}")
        for i, title in enumerate(books.keys()):
            print(f"{i+1}- {title}")
        print("تم عرض جميع الكتب")

def search_book():
    """البحث عن كتاب بالعنوان"""
    print("البحث عن كتاب بالعنوان")
    title = input("أدخل عنوان الكتاب: ").strip()
    if title in books:
        print(f"الكتاب موجود في المكتبة")
        print(f"عنوان الكتاب: {title}")
        print(f"إسم المؤلف: {books[title]['author']}")
        print(f"سنة النشر: {books[title]['year']}")
    else:
        print(f"هذا الكتاب: '{title}' غير موجود في المكتبة")

def delete_book():
    """حذف كتاب"""
    view_books()
    print("حذف كتاب من المكتبة")
    title = input("أدخل عنوان الكتاب: ").strip()
    if title in books:
        del books[title]
        print(f"تم حذف الكتاب: {title} من المكتبة")
        with open("D://Learn/Python/books.txt", "w", encoding='utf-8') as file:
            for title, details in books.items():
                file.write(f"📘 عنوان الكتاب: {title}" + "\n")
                file.write(f"✍️ إسم المؤلف: {details['author']}" + "\n")
                file.write(f"📅 سنة النشر: {details['year']}" + "\n")
                file.write(f"-" * 20 + "\n")
    else:
        print(f"هذا الكتاب: '{title}' غير موجود في المكتبة")

def save_books():
    """حفظ الكتب في ملف نصي"""
    print("حفظ الكتب في ملف نصي")
    if not books:
        print("لا توجد كتب في المكتبة")
    else:
        with open("D://Learn/Python/books.txt", "w", encoding='utf-8') as file:
            for title, details in books.items():
                file.write(f"📘 عنوان الكتاب: {title}" + "\n")
                file.write(f"✍️ إسم المؤلف: {details['author']}" + "\n")
                file.write(f"📅 سنة النشر: {details['year']}" + "\n")
                file.write(f"-" * 20 + "\n")
            print(f"تم حفظ الكتب في ملف نصي بنجاح")

def main():
    """الواجهة الرئيسية للتطبيق"""
    while True:
        print("=" * 50)
        print("📚  تطبيق ادارة مكتبة الكتب".center(50))
        print("=" * 50)
        print("1- إضافة كتاب جديد")
        print("2- عرض جميع الكتب")
        print("3- البحث عن كتاب بالاسم")
        print("4- حذف كتاب")
        print("5- حفظ الكتب في ملف نصي")
        print("6- خروج من التطبيق")
        choice = input("إختر رقم العملية لتنفيذها: ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            save_books()
        elif choice == "6":
            print("خروج من التطبيق")
            break
        else:
            print("إختيار غير صحيح, حاول مرة أخرى")

main()