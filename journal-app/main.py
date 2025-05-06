# -------------
# -- Journal --
# -------------

"""
📓 تطبيق دفتر اليوميات
---------------------
1- ✍️ إضافة مذكرة جديدة
2- 📖 عرض المذكرات
3- 🧹 حذف المذكرات
4- 🚪 خروج من التطبيق
"""

from datetime import datetime

def add_note(): # لإضافة ملاحظة جديدة
    print("✍️ إضافة ملاحظة جديدة")
    note = input("أدخل الملاحظة: ").strip()
    if note:
        with open(r"D://Learn/Python/Notes.txt", "a", encoding="utf-8") as file:
            # كتابة التاريخ و الوقت الحاليين
            file.write(f"📅 التاريخ: {datetime.now().strftime("%d-%m-%Y")} | 🕐 الساعة: {datetime.now().strftime("%H:%M:%S")}")
            file.write(f"\n{note}\n")
            file.write("-" * 50 + "\n")
            print("✅ تمت إضافة الملاحظة بنجاح")
    else:
        print("❌ يجب إدخال ملحظة")

def view_notes(): # دالة لعرض الملاحظات
    print("📖 عرض الملاحظات")
    try:
        file = open(r"D://Learn/Python/Notes.txt", "r", encoding="utf-8")
        notes = file.read()
        if notes:
            print(notes)
        else:
            print("❌ لا توجد ملاحظات")
    except FileNotFoundError:
        print("❌ لا توجد ملاحظات بعد")
    finally:
        file.close()

def delete_notes(): # دالة لحذف جميع الملاحظات
    print("🧹 حذف المذكرات")
    confirm = input("هل أنت متأكد أنك تريد حذف جميع الملاحظات؟ (نعم/لا): ").strip()
    if confirm == "نعم":
        try:
            file = open(r"D://Learn/Python/Notes.txt", "w", encoding="utf-8")
            file.write("") # لحذف جميع الملاحظات
            print("✅ تم حذف جميع الملاحظات بنجاح")
        except FileNotFoundError:
            print("❌ لا توجد ملاحظات لحذفها")
        finally:
            file.close()
    else:
        print("❌ لم يتم حذف الملاحظات")

def main(): # دالة رئسية لتشغيل التطبيق
    while True:
        print("\n" + "=" * 50)
        print("📓 تطبيق دفتر اليوميات".center(50))
        print("=" * 50)
        print("1- ✍️ إضافة مذكرة جديدة")
        print("2- 📖 عرض المذكرات")
        print("3- 🧹 حذف المذكرات")
        print("4- 🚪 خروج من التطبيق")
        choice = input("إختر خيار (1-4): ").strip()
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("🚪 خروج من التطبيق")
            break
        else:
            print("❌ خيار غير صحيح, يرجى المحاولة مرة اخرى")

main() # تشغيل التطبيق
# تم بحمدالله
