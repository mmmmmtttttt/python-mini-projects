# --------------
# -- Contacts --
# --------------

"""
تطبيق لإدارة جهات الاتصال
-------------------------
1- إضافة جهة اتصال (اسم، رقم، بريد).
2- عرض جهات الاتصال.
3- البحث عن جهة اتصال بالاسم.
4- حذف جهة اتصال.
5- حفظ جهات الاتصال في ملف نصي.
6- خروج من التطبيق.
"""

contacts = {}
i = 1

def add_contact():
    name = input("أدخل اسم جهة الاتصال: ").strip().capitalize()
    if name in contacts:
        print("جهة الاتصال موجودة بالفعل.")
        return
    else:
        number = input("أدخل رقم جهة الاتصال: ").strip()
        if not number.isdigit():
            print("رقم الهاتف يجب أن يكون أرقام فقط.")
            return
        if len(number) != 10:
            print("رقم الهاتف يجب أن يتكون من 10 أرقام.")
            return
        if number in [contact["number"] for contact in contacts.values()]:
            print("رقم الهاتف موجود بالفعل.")
            return
        email = input("أدخل بريد جهة الاتصال: ").strip()
        if "@" not in email or "." not in email:
            print("البريد الالكتروني غير صحيح.")
            return
        if email in [contact["email"] for contact in contacts.values()]:
            print("البريد الالكتروني موجود بالفعل.")
            return
        contacts[name] = {"name": name, "number": number, "email": email}
        print(f"تمت إضافة جهة الاتصال: {name}")
        print("الحالة الحالية لجهة الاتصال", contacts)

def view_contacts():
    if not contacts:
        print("لا توجد جهات اتصال.")
        return
    print("جهات الاتصال:")
    for i, contact in enumerate(contacts.values(), start=1):
        print(f"{i}- {contact["name"]} - {contact["number"]} - {contact["email"]}")
    
def search_contact():
    name = input("أدخل اسم جهات الاتصال للبحث: ").strip().capitalize()
    fond = False
    for contact in contacts.values():
        if contact["name"] == name:
            print(f"تم العثور على جهة الاتصال: {contact["name"]} - {contact["number"]} - {contact["email"]}")
            fond = True
            break
    if not fond:
        print("جهة الاتصال غير موجودة")

def delete_contact():
    if not contacts:
        print("لا توجد جهات اتصال لحذفها")
        return
    print("جهات الاتصال المتاحة:")
    view_contacts()

    name = input("أدخل اسم جهة الاتصال لحذفها: ").strip().capitalize()

    # تحقق إذا الاسم موجود كمفتاح
    found = False
    for key in list(contacts.keys()):  # ضروري نحول المفاتيح إلى قائمة قبل الحذف
        if contacts[key]["name"] == name:
            del contacts[key]
            found = True
            print(f"✅ تم حذف جهة الاتصال: {name}")
            break

    if found:
        with open("D://Learn/Python/Contacts.txt", "w", encoding="utf-8") as file:
            for contact in contacts.values():
                file.write(f"{contact['name']}\n")
                file.write(f"- {contact['number']}\n")
                file.write(f"- {contact['email']}\n")
                file.write("-" * 20 + "\n")
    else:
        print("❌ جهة الاتصال غير موجودة")

    print("📦 الحالة الحالية لجهات الاتصال:", contacts)


def save_contacts():
    file = open("D://Learn/Python/Contacts.txt", "w", encoding="utf-8")
    try:
        for contact in contacts.values():
            file.write(f"{contact["name"]}\n")
            file.write(f"- {contact['number']}\n")
            file.write(f"- {contact['email']}\n")
            file.write("-" * 20 + "\n")
            print("تم حفظ جهات الاتصال في الملف.")
    except Exception as e:
        print(f"حدث خطأ أثناء حفظ جهات الاتصال: {e}")
    finally:
        file.close()

def main():
    while True:
        print("=" * 50)
        print("مرحباً بك في تطبيق إدارة جهات الاتصال".center(50))
        print("=" * 50)
        print("1- إضافة جهة اتصال (اسم، رقم، بريد).")
        print("2- عرض جهات الاتصال.")
        print("3- البحث عن جهة اتصال بالاسم.")
        print("4- حذف جهة اتصال.")
        print("5- حفظ جهات الاتصال في ملف نصي.")
        print("6- خروج من التطبيق.")
        choice = input("اختر خيارأً (1-6): ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            save_contacts()
        elif choice == "6":
            print("خروج من التطبيق")
            break
        else:
            print("خيار غير صحيح, يرجى اختيار خيار صحيح (1-6)")

main()