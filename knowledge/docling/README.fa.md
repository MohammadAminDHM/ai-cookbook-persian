# خط لوله استخراج دانش با اسناد

[Docling] (https://github.com/ds4sd/docling) یک کتابخانه پردازش منبع باز قدرتمند و انعطاف پذیر است که قالب های مختلف اسناد را به یک قالب یکپارچه تبدیل می کند.این قابلیت های درک پیشرفته اسناد را با استفاده از مدل های پیشرفته AI برای تجزیه و تحلیل طرح و تشخیص ساختار جدول ارائه داده است.

کل سیستم به صورت محلی روی رایانه های استاندارد کار می کند و به گونه ای طراحی شده است که قابل توسعه باشد - توسعه دهندگان می توانند مدل های جدیدی را اضافه کنند یا خط لوله را برای نیازهای خاص اصلاح کنند.این امر به ویژه برای کارهایی مانند جستجوی اسناد سازمانی ، بازیابی گذرگاه و استخراج دانش مفید است.با قابلیت های پیشرفته و پردازش پیشرفته ، این ابزار مناسب برای ارائه برنامه های Genai با دانش از طریق خطوط لوله Rag (تولید تقویت شده) است.

## ویژگی های کلیدی

- ** پشتیبانی از فرمت جهانی **: فرآیند PDF ، DOCX ، XLSX ، PPTX ، Markdown ، HTML ، تصاویر و موارد دیگر
- ** درک پیشرفته **: تجزیه و تحلیل طرح بندی شده با AI و تشخیص ساختار جدول
- ** خروجی انعطاف پذیر **: صادرات به HTML ، Markdown ، JSON یا متن ساده
- ** با کارایی بالا **: پردازش کارآمد در سخت افزار محلی

## چیزهایی که آنها روی آن کار می کنند

- استخراج ابرداده ، از جمله عنوان ، نویسندگان ، منابع و زبان
- گنجاندن مدل های زبان بصری (Smoldocling)
- درک نمودار (Barchart ، PieChart ، LinePlot و غیره)
- درک شیمی پیچیده (ساختارهای مولکولی)

## شروع با مثال

### پیش نیازها

1. بسته های مورد نیاز را نصب کنید:

`` `bash
pip install -r نیاز. txt
`` `

2. متغیرهای محیط خود را با ایجاد یک پرونده `.env` تنظیم کنید:

`` `bash
Openai_api_key = your_api_key_here
`` `

### اجرای مثال

برای ساختن و پرس و جو از پایگاه داده سند ، پرونده ها را اجرا کنید:

1. محتوای سند عصاره: `Python 1-Extraction.py`
2. ایجاد بخش های سند: `Python 2-chunking.py`
3. تعبیه کنید و در LancedB ذخیره کنید: `Python 3-Embedding.py`
4. آزمایش عملکرد اصلی جستجوی: `Python 4-search.py`
5. رابط چت StreamLit را راه اندازی کنید: `streamlit run 5-chat.py`

سپس مرورگر خود را باز کرده و به `http: // localhost: 8501` بروید تا با رابط Q&A سند تعامل داشته باشید.

## پردازش سند

### قالب های ورودی پشتیبانی شده

|قالب |توضیحات |
| -------- | ------------- |
|PDF |اسناد بومی PDF با حفظ طرح |
|DOCX ، XLSX ، PPTX |قالب های مایکروسافت آفیس (2007+) |
|Markdown |متن ساده با Markup |
|html/xhtml |اسناد وب |
|تصاویر |PNG ، JPEG ، TIFF ، BMP |
|USPTO XML |اسناد ثبت اختراع |
|PMC XML |مقالات مرکزی PubMed |

برای لیست به روز ، این [صفحه] (https://ds4sd.github.io/docling/supported_formats/) را بررسی کنید.

خط لوله ### پردازش

خط لوله استاندارد شامل موارد زیر است:

1. تجزیه و تحلیل سند با باکتری خاص فرمت
2. تجزیه و تحلیل طرح با استفاده از مدل های AI
3. شناخت ساختار جدول
4. استخراج ابرداده
5. سازمان و ساختار محتوا
6. قالب بندی صادرات

## مدل ها

Docling دو مدل اصلی AI تخصصی را برای درک اسناد اعمال می کند.در هسته آن ، مدل تجزیه و تحلیل طرح بر روی معماری "RT-DETER (ترانسفورماتور تشخیص زمان واقعی)) ساخته شده است ، که در تشخیص و طبقه بندی عناصر صفحه عالی است.این مدل صفحات را با وضوح 72 DPI پردازش می کند و می تواند یک صفحه واحد را در زیر یک ثانیه در یک پردازنده استاندارد تجزیه و تحلیل کند ، که در مجموعه داده های جامع "Doclaynet" آموزش دیده است.

مدل دوم کلید "TableFormer" ، یک سیستم تشخیص ساختار جدول است که می تواند طرح های پیچیده جدول از جمله مرزهای جزئی ، سلولهای خالی ، سلولهای پوششی و هدرهای سلسله مراتبی را کنترل کند.TableFormer به طور معمول جداول را در 2-6 ثانیه در CPU پردازش می کند و آن را برای استفاده عملی کارآمد می کند.

برای اسنادی که نیاز به استخراج متن از تصاویر دارند ، اسناد "Easyocr" را به عنوان یک مؤلفه اختیاری ادغام می کنند ، که برای کیفیت بهینه در 216 dpi کار می کند اما در هر صفحه حدود 30 ثانیه نیاز دارد.هر دو مدل تجزیه و تحلیل طرح و جدول TableFormer توسط IBM Research تهیه شده و به عنوان وزنهای از قبل آموزش دیده در بغل کردن صورت U در دسترس عموم هستندnder "DS4SD/مدلهای اسناد".

برای کسب اطلاعات بیشتر در مورد این مدل ها و اجرای آنها ، می توانید به [اسناد فنی] (https://arxiv.org/pdf/2408.09869) مراجعه کنید.

##

هنگامی که شما در حال ساختن یک برنامه RAG (نسل تقویت شده بازیابی) هستید ، باید اسناد را به قطعات کوچکتر و معنی دار تقسیم کنید که به راحتی قابل جستجو و بازیابی هستند.اما این ساده نیست که فقط متن را تقسیم کنید هر کلمه یا شخصیت.

چیزی که باعث می شود [chunking docling] (https://ds4sd.github.io/docling/concepts/chunking/) منحصر به فرد باشد این است که ساختار واقعی سند شما را درک می کند.این دو رویکرد اصلی دارد:

1. [chunker سلسله مراتبی] (https://ds4sd.github.io/docling/concepts/chunking/#hierarchical -chunker) مانند یک آنالایزر اسناد هوشمند است - می داند "مفاصل" طبیعی سند شما کجاست.به جای برش کورکورانه متن را به قطعات با اندازه ثابت ، عناصر مهمی مانند بخش ها ، پاراگراف ها ، جداول و لیست ها را تشخیص و حفظ می کند.این رابطه بین هدرها و محتوای آنها را حفظ می کند و موارد مرتبط را در کنار هم نگه می دارد (مانند موارد در یک لیست).

2. [chunker hybrid] (https://ds4sd.github.io/docling/concepts/chunking/#yhybrid-chunker) این قدم را بیشتر برداشته است.این با بخش های سلسله مراتبی شروع می شود اما پس از آن:
- می تواند تکه هایی را که برای مدل تعبیه شما بسیار بزرگ است تقسیم کند
- می تواند تکه هایی را که خیلی کوچک هستند ، بخیه بزنند
- با توکینر خاص شما کار می کند ، بنابراین تکه ها کاملاً با مدل زبان انتخاب شده شما مطابقت دارند

### چرا این برای برنامه های RAG عالی است؟

تصور کنید که در حال ایجاد سیستمی برای پاسخ به سؤالات مربوط به اسناد فنی هستید.با استفاده از تکه های اساسی (مانند تقسیم هر 500 کلمه) ، ممکن است درست از وسط یک جدول بریده شوید ، یا یک هدر را از محتوای آن جدا کنید.اما تکه های هوشمند Docling:

- اطلاعات مرتبط را با هم نگه می دارد
- ساختار سند را حفظ می کند
- زمینه را حفظ می کند (مانند هدرها و زیرنویس ها)
- تکه هایی را ایجاد می کند که برای مدل تعبیه خاص شما بهینه شده اند
- تضمین می کند که هر تکه معنی دار و خود است

این بدان معناست که وقتی سیستم RAG شما قطعات را بازیابی می کند ، آنها زمینه و ساختار مناسب را خواهند داشت و منجر به پاسخ های دقیق تر و منسجم از مدل زبان شما می شوند.

## مستندات

برای مستندات کامل ، به [سایت اسناد] مراجعه کنید (https://ds4sd.github.io/docling/).

به عنوان مثال نوت بوک ها و راهنماهای دقیق تر ، [مخزن GitHub] (https://github.com/ds4sd/docling) را بررسی کنید.