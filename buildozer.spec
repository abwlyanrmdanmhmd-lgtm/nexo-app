[app]
# اسم التطبيق
title = Ammar Ya Misr
# اسم الحزمة (لازم يكون انجليزي وبدون مسافات)
package.name = ammaryamisr
# الدومين
package.domain = org.ramadan

# مكان ملفات الكود
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# الإصدار
version = 0.1

# المتطلبات (المكتبات اللي بيحتاجها الكود)
requirements = python3,kivy

# اتجاه الشاشة
orientation = portrait

# إعدادات الأندرويد
android.arch = armeabi-v7a
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1