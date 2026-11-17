# راه‌اندازی آزمایشگاه جدید jq برای PatchGuard

این نسخه نسبت به بستهٔ راه‌انداز اولیه اصلاح شده است: 
* در بیلد checked از `-fno-pie` و `-no-pie` استفاده می‌شود.
* در فایل `tooling/PGMakefile` پیش از `autoreconf` دایرکتوری لازم ایجاد و سپس `make -f Makefile all` اجرا می‌شود.
* در هر دو workflow شناسهٔ اکشن به صورت `__PATCHGUARD_SHA__` باقی مانده و باید پیش از اولین push با کامیت نهایی منتشرشدهٔ PatchGuard جایگزین شود.

## کامیت‌های upstream jq
A: `c5fd64ba975ee35df17bb0c335efb00bffce4d91`
B: `c9a51565214eece8f1053089739aea73145bfd6b`
C: `71c2ab509a8628dbbad4bc7b3f98a64aa90d3297`

## ترتیب آزمایش‌های مخزن جدید
1. روی main فقط A را وارد کن و هیچ تست رگرسیون قدیمی را کپی نکن.
2. شاخهٔ `experiment/jq-A-to-B` را از main بساز و B را وارد کن؛ PR به main با انتظار کد ۱۰.
3. ZIP شواهد A→B را ذخیره کن و PR خودکار شامل تست‌های کوچک‌شده را بازبینی/ادغام کن.
4. از main تازه‌شده شاخهٔ پایهٔ `lab/jq-base-B` بساز و B را وارد کن.
5. از آن شاخه `experiment/jq-B-to-C` بساز و C را وارد کن؛ PR به `lab/jq-base-B` (نه main) با انتظار کد صفر.
6. ZIP شواهد B→C را ذخیره کن.

## واردکردن نسخه
از ریشهٔ مخزن جدید، پس از قراردادن `jq-upstream` در پوشهٔ خواهرش، از دستور زیر استفاده کن:
`bash scripts/import_jq_revision.sh FULL_UPSTREAM_SHA`

## نکتهٔ Oracle
`tests/oracle_jq.py` فقط زیرمجموعهٔ مستند و محدودی از رفتار jq را مدل می‌کند و نباید با استناد به خروجی Candidate به‌صورت خودکار گسترش پیدا کند.
