# -*- coding: utf-8 -*-
"""Arabic copy for the ELITƎ site.

Where gc-elite.com already publishes Arabic (the About page, the contact intro,
the footer summary, the navigation), that wording is reproduced verbatim so the
two sites read the same. Everything the live site leaves untranslated — the
service descriptions, the dashboard, the success stories, the client roster — is
translated here in the same register.

KEEP lists strings that stay in Latin script on an Arabic page: the wordmark,
brand names, figures and units. The live Arabic site does the same.
"""

KEEP = {
    # The deployed Arabic build translates the tagline, so it is copy, not a
    # Latin lockup. It lives in AR below.
    "Elite", "ELITƎ", "ELIT", "E", "AR", "EN",
    "24.9M", "17.9M", "13.9M", "206.2K", "930", "40", "10", "75",
    "you@example.com", "you@company.com", "+966 …",
    "Copyright ©",
}

AR = {
    # ── head / meta ─────────────────────────────────────────────────────────
    "Elite — Niche Mastery Redefined":
        "إيليت — منصة المؤثرين التي تعتمد عليها العلامات الفاخرة",
    "Elite is the #1 influencer marketing platform: creator discovery, campaign strategy, content creation and performance tracking across 52+ countries.":
        "تربط إيليت العلامات التجارية الفاخرة بصنّاع محتوى موثوقين في أكثر من 52 دولة، ثم تخطط للحملة وتديرها وتقيس نتائجها في مساحة عمل واحدة.",
    "Dashboard — Elite":
        "مساحة العمل — إيليت",
    "Success Stories — Elite": "قصص النجاح — إيليت",
    "Our Clients — Elite": "عملاؤنا — إيليت",
    "Contact Us — Elite": "تواصل معنا — إيليت",
    "About Us — Elite": "من نحن — إيليت",

    # ── chrome ──────────────────────────────────────────────────────────────
    "Skip to content": "تخطَّ إلى المحتوى",
    "Elite — home": "إيليت — الصفحة الرئيسية",
    "Primary": "التنقّل الرئيسي",
    "Home":
        "الرئيسية",
    "Dashboard":
        "مساحة العمل",
    "Success Stories": "قصص النجاح",
    "Our Clients": "عملاؤنا",
    "Contact Us": "تواصل معنا",
    "About Us": "من نحن",
    "Switch language to Arabic": "التبديل إلى اللغة الإنجليزية",
    "Switch theme": "تغيير المظهر",
    "Start a campaign": "ابدأ حملتك",
    "Open menu": "فتح القائمة",
    "Close": "إغلاق",
    "Scroll": "مرِّر",
    "Live": "مباشر",
    "View all": "عرض الكل",
    "All": "الكل",
    "Sign in": "تسجيل الدخول",
    "Contact us": "تواصل معنا",
    "Get in touch":
        "تواصل معنا",
    "Talk to us": "تحدّث إلينا",

    # ── home: hero ──────────────────────────────────────────────────────────
    "Influencer marketing · 52+ countries": "التسويق عبر المؤثرين · أكثر من 52 دولة",
    "Niche mastery,":
        "اعثر على صنّاع المحتوى الأنسب.",
    "redefined.":
        "وأدِر كل حملة من مكان واحد.",
    "Elite connects premium brands with the creators their audience already trusts — then plans, runs and measures the whole campaign for you.":
        "نصلك بصنّاع محتوى يتابعهم عملاؤك فعلًا، وندير الحملة كاملة نيابةً عنك، ونُطلعك بدقة على ما حققته.",
    "See success stories": "اطّلع على قصص النجاح",
    "Years of campaigns": "سنوات من الحملات",
    "Countries covered":
        "دولة نغطيها",
    "Creators on call":
        "صانع محتوى جاهز",
    "Brands served":
        "علامة تجارية خدمناها",
    "Elite campaign signal": "مؤشّر حملات إيليت",
    "Campaign signal": "مؤشّر الحملة",
    "The right voice,": "الصوت المناسب،",
    "in the right room.": "في المكان المناسب.",
    "Audience alignment": "توافق الجمهور",
    "Trusted by category leaders across the Gulf and beyond":
        "أكثر من 75 علامة تجارية فاخرة في الخليج تثق بنا",
    "Pause logo movement": "إيقاف حركة الشعارات",
    "View all 75 clients":
        "شاهد جميع العملاء الـ75",

    # ── home: why elite ─────────────────────────────────────────────────────
    "Why Elite": "لماذا إيليت",
    "Exceptional results need": "النتائج الاستثنائية تحتاج",
    "exceptional strategy.": "إلى استراتيجية استثنائية.",
    "Ten years of relationships with elite influencers and high-end brands, put to work on your campaign.":
        "عشر سنوات من العلاقات مع نخبة المؤثرين والعلامات التجارية الراقية، نضعها في خدمة حملتك.",
    "A decade of excellence": "عقد من التميّز",
    "Over 10 years running influencer campaigns for high-end brands — the playbook is already written.":
        "أكثر من 10 سنوات في إدارة حملات المؤثرين للعلامات الراقية — الخطة مكتوبة سلفًا.",
    "Global reach": "الوصول العالمي",
    "A presence in more than 52 countries connects your brand with the right audience, wherever it lives.":
        "حضورنا في أكثر من 52 دولة يربط علامتك بالجمهور المناسب أينما كان.",
    "Elite partnerships": "شراكات نخبوية",
    "Exclusive relationships with elite creators and premium brands mean access others simply don't have.":
        "علاقات حصرية مع نخبة صنّاع المحتوى والعلامات الراقية تمنحك وصولًا لا يملكه غيرك.",
    "Measurable results": "نتائج قابلة للقياس",
    "Every campaign is tracked end to end, so growth is something you can see — not something you're told.":
        "كل حملة متتبَّعة من أولها إلى آخرها، فالنمو شيء تراه بنفسك لا شيء يُقال لك عنه.",

    # ── home: services ──────────────────────────────────────────────────────
    "Elite service solutions": "حلول خدمات إيليت",
    "Everything a campaign needs,": "كل ما تحتاجه الحملة،",
    "under one roof.": "تحت سقف واحد.",
    "From finding the right creator to proving the return — four services that run as one process.":
        "من العثور على صانع المحتوى المناسب إلى إثبات العائد — أربع خدمات تعمل كعملية واحدة.",
    "Influencer": "مؤثر",
    "Discovery": "الاكتشاف",
    "Tap into our vast network to connect with influencers who perfectly match your brand and audience, boosting engagement and brand affinity.":
        "استفد من شبكتنا الواسعة للتواصل مع مؤثرين يناسبون علامتك وجمهورك تمامًا، بما يرفع التفاعل والارتباط بالعلامة.",
    "Campaign": "حملة",
    "Strategy": "الاستراتيجية",
    "Work with our experts to design influencer campaigns aligned with your goals, ensuring impactful results and brand resonance.":
        "اعمل مع خبرائنا لتصميم حملات مؤثرين متوائمة مع أهدافك، بما يضمن نتائج مؤثرة وصدى حقيقيًا لعلامتك.",
    "Content": "المحتوى",
    "Creation": "الإنتاج",
    "Collaborate with influencers to create compelling content that captivates your audience and drives action.":
        "تعاون مع المؤثرين لصناعة محتوى جذّاب يأسر جمهورك ويدفعه إلى التفاعل.",
    "Performance": "الأداء",
    "Tracking": "التتبّع",
    "Gain actionable insights into campaign performance, optimizing strategies for maximum impact and ROI.":
        "احصل على رؤى عملية حول أداء الحملة، لتحسين الاستراتيجيات وتحقيق أقصى أثر وعائد على الاستثمار.",

    # ── home: how it works ──────────────────────────────────────────────────
    "How it works": "كيف نعمل",
    "Four steps.": "أربع خطوات.",
    "One clear line to results.":
        "من البداية إلى النتيجة.",
    "You bring the brand and the goal. We handle discovery, negotiation, production and reporting — and you see every stage as it happens.":
        "أنت تحدّد الهدف. ونحن نختار صنّاع المحتوى، ونتفق على الشروط، وندير المحتوى، ونرفع لك النتائج — ويتابع فريقك كل ذلك في مكان واحد.",
    "Book a strategy call": "احجز مكالمة استراتيجية",
    "Match": "المطابقة",
    "We shortlist creators from our network whose audience genuinely overlaps with yours.":
        "نختار من شبكتنا صنّاع محتوى جمهورهم هو نفسه الجمهور الذي تريد الوصول إليه.",
    "Plan": "التخطيط",
    "Objectives, budget, markets and deliverables become a campaign brief everyone signs off.":
        "تتحوّل الأهداف والميزانية والأسواق والمخرجات إلى موجز حملة يعتمده الجميع.",
    "Create": "الإنتاج",
    "Creators produce content in their own voice, reviewed against your brand guidelines.":
        "ينتج صنّاع المحتوى موادّهم بأسلوبهم الخاص، وتُراجَع وفق إرشادات علامتك.",
    "Measure": "القياس",
    "Live coverage tracking and post-campaign reporting show exactly what the spend returned.":
        "ترى كل منشور فور نشره، وتستلم تقريرًا واضحًا في النهاية.",

    # ── home: stories ───────────────────────────────────────────────────────
    "Success in action":
        "نتائج عملائنا",
    "Stories from our clients.": "قصص من عملائنا.",
    "All success stories": "كل قصص النجاح",
    "Enigmaku — success story": "Enigmaku — قصة نجاح",
    "Tashas Cafe — success story": "Tashas Cafe — قصة نجاح",
    "Beit El Sabban — success story": "Beit El Sabban — قصة نجاح",
    "Fred — success story": "Fred — قصة نجاح",
    "Kuwait": "الكويت",
    "Saudi Arabia": "السعودية",
    "Reach":
        "وصول الحملة",
    "Creators":
        "صانع محتوى في الشبكة",
    "Followers": "المتابعون",
    "Influencers": "المؤثرون",

    # ── home: dashboard teaser ──────────────────────────────────────────────
    "Favourite influencers": "المؤثرون المفضّلون",
    "▲ Live from your network": "▲ مباشر من شبكتك",
    "Coverage tracked": "التغطية المتتبَّعة",
    "Stories": "ستوري",
    "Posts": "منشورات",
    "Video":
        "ريلز",
    "The Elite dashboard":
        "مساحة عمل إيليت",
    "Your whole campaign,":
        "حملتك كاملة،",
    "on one screen.": "على شاشة واحدة.",
    "Branches, favourite creators, campaign stages, coverage and reporting — all in a single workspace, with 24/7 live support behind it.":
        "كل فرع وصانع محتوى ومنشور في لوحة واحدة. يطّلع فريقك على التقدّم في أي وقت، ويجد شخصًا حقيقيًا للمساندة على مدار الساعة.",
    "Track every creator from pending to covered": "تتبّع كل صانع محتوى من قيد الانتظار حتى اكتمال التغطية",
    "Story, post and video coverage counted automatically": "احتساب تغطية الستوري والمنشورات والفيديو تلقائيًا",
    "Wishlists, branches and scanner tools built in": "قوائم التفضيل والفروع وأدوات المسح مدمجة",
    "Explore the dashboard":
        "استكشف مساحة العمل",

    # ── home: closing band ──────────────────────────────────────────────────
    "Ready to elevate your brand?":
        "أخبرنا بما تريد إطلاقه.",
    "Tell us the goal. We'll come back with the creators, the plan and the numbers — wherever in the world you are.":
        "سنعود إليك بصنّاع المحتوى والخطة والأرقام. عادةً خلال يومين.",

    # ── footer ──────────────────────────────────────────────────────────────
    "About Elite": "نبذة عن إيليت",
    "Elite is the #1 influencer marketing platform to help you achieve all your marketing goals. We launch and manage your campaigns with 24/7 live support.":
        "إيليت هي منصة التسويق عبر المؤثرين التي تعتمد عليها العلامات التجارية الفاخرة للوصول إلى صنّاع المحتوى المناسبين، وإدارة الحملة، وإثبات نتائجها — بدعم مباشر على مدار الساعة.",
    "Elite on Instagram": "إيليت على إنستغرام",
    "Email Elite": "راسل إيليت",
    "Explore": "تصفّح",
    "Company": "الشركة",
    "Privacy Policy": "سياسة الخصوصية",
    "Newsletter":
        "النشرة البريدية",
    "Campaign insights and creator trends, once a month.":
        "رؤى عن الحملات واتجاهات صنّاع المحتوى، مرة واحدة شهريًا. بلا رسائل ترويجية.",
    "Email address": "البريد الإلكتروني",
    "Enter your email": "أدخل بريدك الإلكتروني",
    "Enter a valid email address.":
        "أدخل بريدًا إلكترونيًا صحيحًا، مثل name@company.com.",
    "Subscribe": "اشترك",
    "Elite. All rights reserved.":
        "Elite. جميع الحقوق محفوظة.",
    "Elite collects only the information needed to run your campaigns — contact details you submit, and campaign performance data from connected creator accounts. We never sell your data.":
        "لا تجمع إيليت سوى المعلومات اللازمة لتشغيل حملاتك — بيانات التواصل التي ترسلها، وبيانات أداء الحملة من حسابات صنّاع المحتوى المرتبطة. نحن لا نبيع بياناتك إطلاقًا.",
    "For the full policy, or to request deletion of your data, contact us and we will respond within 30 days.":
        "للاطلاع على السياسة كاملة أو لطلب حذف بياناتك، تواصل معنا وسنرد خلال 30 يومًا.",

    # ── dashboard page ──────────────────────────────────────────────────────
    "One workspace for branches, creators, campaign stages and coverage reporting.":
        "مساحة عمل واحدة للفروع وصنّاع المحتوى ومراحل الحملة وتقارير التغطية.",
    "DASHBOARD":
        "مساحة العمل",
    "One workspace for every campaign":
        "حملتك كاملة، على شاشة واحدة",
    "Branches, creators, campaign stages and coverage — the Elite platform gives you a comprehensive overview of all influencer marketing activities.":
        "الفروع وصنّاع المحتوى ومراحل الحملة والتغطية — تمنحك إيليت رؤية شاملة واحدة لكل نشاط تسويقي عبر المؤثرين.",
    "Sign in to your dashboard":
        "ادخل إلى لوحة التحكم",
    "Request a demo": "اطلب عرضًا توضيحيًا",
    "Interactive preview": "معاينة تفاعلية",
    "Illustrative campaign data — switch a view to explore the workspace.":
        "بيانات حملة توضيحية — بدّل العرض لاستكشاف مساحة العمل.",
    "Choose a dashboard demo campaign": "اختر حملة توضيحية للوحة التحكم",
    "Summer launch": "إطلاق الصيف",
    "Always-on growth": "نمو مستمر",
    "New location": "فرع جديد",
    "Summer launch · Riyadh": "إطلاق الصيف · الرياض",
    "01–30 Jun 2026": "1–30 يونيو 2026",
    "Branches": "الفروع",
    "Per location reporting": "تقارير لكل فرع",
    "Your saved network": "شبكتك المحفوظة",
    "Campaigns": "الحملات",
    "Live and scheduled": "الجارية والمجدولة",
    "Coverage": "التغطية",
    "Stories · posts · video": "ستوري · منشورات · فيديو",
    "Influencer overview":
        "نظرة على المؤثرين",
    "Every creator, every stage.":
        "كل صانع محتوى، في كل مرحلة.",
    "Follow each influencer from first contact to published coverage, without chasing anyone for an update.":
        "تابع كل مؤثر من أول تواصل حتى نشر التغطية، دون مطاردة أحد للحصول على تحديث.",
    "Creator campaign stages": "مراحل الحملة لصانع المحتوى",
    "Pending": "قيد الانتظار",
    "Confirmed": "مؤكَّد",
    "Visited": "تمت الزيارة",
    "Delivered": "تم التسليم",
    "Post creation":
        "إنشاء المحتوى",
    "Shared":
        "تم النشر",
    "Covered":
        "اكتملت التغطية",
    "Live workspace": "مساحة عمل مباشرة",
    "Recent campaigns": "أحدث الحملات",
    "Coverage details": "تفاصيل التغطية",
    "346 pieces": "346 قطعة محتوى",
    "Story": "ستوري",
    "Post": "منشور",
    "Coverage is grouped by format and updates with the selected demo campaign.":
        "التغطية مجمَّعة حسب الصيغة وتتحدّث مع الحملة التوضيحية المختارة.",
    "Inside the platform": "داخل المنصة",
    "Built for people running campaigns.":
        "مبنية لمن يديرون الحملات فعلًا.",
    "Influencers & wishlist":
        "المؤثرون والمفضلة",
    "Browse the network, save favourites and build shortlists your whole team can see.":
        "تصفّح الشبكة، واحفظ المفضلين، وابنِ قوائم يراها فريقك كاملًا.",
    "Run multi-location brands with coverage and check-ins tracked per branch.":
        "أدر العلامات متعددة الفروع مع تتبع التغطية وتسجيل الحضور لكل فرع.",
    "Scanner": "الماسح",
    "Verify creator check-ins on site with a quick scan — no paperwork.":
        "تحقّق من حضور صنّاع المحتوى في الموقع بمسح سريع — بلا أوراق.",
    "Brief, approve and monitor every campaign stage in one timeline.":
        "جهّز الموجز، واعتمد، وراقب كل مرحلة في مسار زمني واحد.",
    "Reporting": "التقارير",
    "Coverage by format and creator, ready to share with stakeholders.":
        "تغطية حسب النوع وصانع المحتوى والفرع — جاهزة للمشاركة مع أصحاب القرار.",
    "24/7 support": "دعم على مدار الساعة",
    "A live team behind the platform whenever a campaign needs a hand.":
        "مدير معروف بالاسم من إيليت خلف المنصة كلما احتاجت الحملة إلى مساندة.",
    "See it with your own campaign.":
        "شاهدها بحملتك أنت.",
    "Sign in to your workspace, or ask us for a walkthrough with your brand's data.":
        "سجّل الدخول إلى مساحة عملك، أو اطلب منا جولة ببيانات علامتك.",

    # ── success stories page ────────────────────────────────────────────────
    "Success in action: influencer campaigns Elite has run for premium brands, with reach and creator counts.":
        "حملات مؤثرين نفّذتها إيليت لعلامات فاخرة، بنتائج وصول واضحة.",
    "SUCCESS IN ACTION":
        "قصص النجاح",
    "Stories From Our Clients":
        "النجاح في الميدان",
    "Real campaigns, real creators, real numbers. Filter by category to find work close to yours.":
        "نتائج حملات حقيقية، بأرقام واضحة. اختر التصنيف للاطلاع على أعمال أقرب إلى احتياج علامتك.",
    "Search success stories": "ابحث في قصص النجاح",
    "Search stories…": "ابحث في القصص…",
    "Restaurant": "مطاعم",
    "Café": "مقاهٍ",
    "Cafe": "مقاهٍ",
    "Fashion": "أزياء",
    "Beauty": "تجميل",
    "Perfume": "عطور",
    "No stories in this category yet":
        "لا توجد قصص في هذا التصنيف بعد",
    "Try another filter, or tell us what you're looking for and we'll share relevant work directly.":
        "جرّب تصفية أخرى، أو أخبرنا بما تبحث عنه ونشاركك أعمالًا مناسبة مباشرةً.",
    "Request case studies": "اطلب دراسات الحالة",
    "Nothing matched that search": "لا نتائج مطابقة لهذا البحث",
    "Check the spelling, or clear the search to see every story.":
        "تحقّق من الإملاء، أو امسح البحث لعرض كل القصص.",
    "Get a campaign like these": "احصل على حملة مثل هذه",
    "Questions": "أسئلة",
    "How a campaign runs.": "كيف تُدار الحملة.",
    "How do you pick the creators?": "كيف تختارون صنّاع المحتوى؟",
    "We shortlist from our network based on genuine audience overlap with your brand — market, category, age profile and engagement quality — not follower count alone.":
        "نختار من شبكتنا بناءً على تقاطع حقيقي بين الجمهور وعلامتك — السوق والفئة والشريحة العمرية وجودة التفاعل — لا عدد المتابعين وحده.",
    "How long does a campaign take?": "كم تستغرق الحملة؟",
    "It depends on scope and market, but most campaigns move from brief to first published content within a few weeks. We'll give you a schedule before anything is signed.":
        "يعتمد ذلك على النطاق والسوق، لكن معظم الحملات تنتقل من الموجز إلى أول محتوى منشور خلال أسابيع قليلة. وسنمنحك جدولًا زمنيًا قبل توقيع أي شيء.",
    "What do you report back?": "ماذا تقدّمون في التقارير؟",
    "Coverage by creator and format — stories, posts and video — plus reach and campaign-level performance, all visible live in the Elite dashboard.":
        "التغطية حسب صانع المحتوى والصيغة — ستوري ومنشورات وفيديو — إضافةً إلى الوصول وأداء الحملة، وكلها ظاهرة مباشرةً في لوحة تحكم إيليت.",
    "Which markets do you cover?": "ما الأسواق التي تغطّونها؟",
    "Elite has a presence in more than 52 countries, with the deepest creator networks across Saudi Arabia, Kuwait, the UAE, Qatar and Bahrain.":
        "لإيليت حضور في أكثر من 52 دولة، مع أعمق شبكات صنّاع المحتوى في السعودية والكويت والإمارات وقطر والبحرين.",

    # ── clients page ────────────────────────────────────────────────────────
    "Seventy-five brands across seven countries and twelve categories partner with Elite for influencer marketing.":
        "خمس وسبعون علامة تجارية في سبع دول واثني عشر قطاعًا تتعاون مع إيليت.",
    "OUR CLIENTS": "عملاؤنا",
    "Seventy-five brands across seven countries and twelve categories choose Elite to reach their audience.":
        "من مطابخ ميشلان إلى صنّاع الساعات السويسريين — العلامات التي تأتمن إيليت على برامجها مع صنّاع المحتوى.",
    "All clients": "كل العملاء",
    "Countries":
        "دولة نغطّيها",
    "Categories": "الفئات",
    "Clients by category":
        "العملاء حسب القطاع",
    "Cosmetics / Beauty": "مستحضرات التجميل",
    "Clients by region": "العملاء حسب المنطقة",
    "United Arab Emirates": "الإمارات",
    "Qatar": "قطر",
    "Bahrain": "البحرين",
    "The roster": "القائمة",
    "Brands we work with.": "العلامات التي نعمل معها.",
    "Search clients": "ابحث في العملاء",
    "Search clients…":
        "ابحث باسم العلامة",
    "No clients in this category yet": "لا يوجد عملاء في هذه الفئة بعد",
    "Pick another category to keep browsing.": "اختر فئة أخرى لمواصلة التصفّح.",
    "No match for that name": "لا تطابق لهذا الاسم",
    "Clear the search to see the full roster.": "امسح البحث لعرض القائمة كاملة.",
    "Showing all 75 clients":
        "بعض العلامات التي نعمل معها",
    "Your brand belongs here.": "مكان علامتك هنا.",
    "Join seventy-five brands running influencer campaigns with Elite across the Gulf and beyond.":
        "انضم إلى خمس وسبعين علامة تجارية تدير حملات المؤثرين مع إيليت في الخليج وخارجه.",
    "Become a client": "كن عميلًا",

    # ── contact page ────────────────────────────────────────────────────────
    "Talk to Elite about an influencer campaign, or join the network as a creator. 24/7 live support.":
        "تحدّث إلى إيليت بشأن حملة مؤثرين، أو انضم إلى الشبكة كصانع محتوى.",
    "CONTACT US": "تواصل معنا",
    "Stay connected with us! Whether you have a question, suggestion, or just want to say hello, we're here to help. Don't hesitate to reach out — we'd love to hear from you.":
        "وسنعود إليك بصنّاع المحتوى والخطة والأرقام — عادةً خلال 48 ساعة.",
    "I am a": "أنا",
    "Brand": "علامة تجارية",
    "Join the Elite network and work with the region's premium brands.":
        "انضم إلى شبكة إيليت واعمل مع أرقى علامات المنطقة.",
    "Name":
        "اسمك",
    "Your full name": "اسمك الكامل",
    "Please enter your name.":
        "أدخل اسمك الكامل.",
    "Country": "الدولة",
    "Select country": "اختر الدولة",
    "Egypt": "مصر",
    "Other": "أخرى",
    "Email": "البريد الإلكتروني",
    "Phone number":
        "رقم الجوال",
    "WhatsApp is active on this number": "واتساب مُفعَّل على هذا الرقم",
    "Message":
        "ما الذي تخطط له؟",
    "Tell us about your audience and the brands you'd like to work with.":
        "أخبرنا عن جمهورك والعلامات التي تودّ العمل معها.",
    "Send message": "إرسال الرسالة",
    "Tell us the goal and we'll come back with creators, a plan and a budget.":
        "أخبرنا بالهدف ونعود إليك بصنّاع المحتوى والخطة والميزانية.",
    "Brand name": "اسم العلامة التجارية",
    "Please enter your brand.":
        "أدخل اسم الشركة.",
    "Category": "الفئة",
    "Select category": "اختر الفئة",
    "Hotel": "فنادق",
    "What are you launching, and what does success look like?":
        "ما الذي تطلقه، وكيف يبدو النجاح بالنسبة لك؟",
    "What happens next": "ماذا يحدث بعد ذلك",
    "We read your brief and check creator fit.": "نقرأ موجزك ونتحقّق من ملاءمة صنّاع المحتوى.",
    "You get a shortlist, a plan and a budget.": "تصلك قائمة مختصرة وخطة وميزانية.",
    "We run the campaign and report live.": "ندير الحملة ونرفع التقارير مباشرةً.",
    "Where we work": "أين نعمل",
    "Saudi Arabia · Kuwait · United Arab Emirates · Qatar · Bahrain — and 52+ countries worldwide.":
        "السعودية · الكويت · الإمارات · قطر · البحرين — وأكثر من 52 دولة حول العالم.",
    "24/7 live support": "دعم مباشر على مدار الساعة",
    "Campaigns don't keep office hours. Neither do we.":
        "الحملات لا تلتزم بساعات العمل، ونحن كذلك.",

    # ── about page (live-site Arabic, verbatim) ─────────────────────────────
    "Over a decade of influencer marketing across more than 52 countries. Elite's mission, approach and reasons brands stay.":
        "أكثر من عقد في التسويق عبر المؤثرين في ما يزيد على 52 دولة.",
    "ABOUT US": "من نحن",
    "Your premier destination for cutting-edge influencer marketing solutions.":
        "أمضت إيليت أكثر من عشر سنوات في بناء العلاقات التي تُنجح حملات المؤثرين — مع صنّاع المحتوى، ومع العلامات التي يمثلونها.",
    "Who we are": "من نحن",
    "A decade of influence,":
        "عقدٌ من إتقان التخصص،",
    "in more than 52 countries.": "في أكثر من 52 دولة.",
    "Welcome to Elite. With over a decade of experience in the industry and a global presence spanning more than 52 countries, Elite has established itself as a trusted leader in the world of influencer marketing. Our extensive experience and international reach empower us to deliver unparalleled results for brands seeking to maximize their impact on a global scale.":
        "مرحبًا بك في Elite، وجهتك الأولى للحصول على حلول تسويق مؤثرة متطورة. بفضل أكثر من عقد من الخبرة في الصناعة وحضور عالمي يمتد لأكثر من 52 دولة، أثبتت Elite نفسها كقائد موثوق به في عالم تسويق المؤثرين. تمكننا خبرتنا الواسعة وانتشارنا الدولي من تقديم نتائج لا مثيل لها للعلامات التجارية التي تسعى إلى تعظيم تأثيرها على نطاق عالمي.",
    "Years":
        "سنة من الحملات",
    "Brands":
        "علامة تجارية خدمناها",
    "Our mission":
        "رسالتنا",
    "Simple, yet powerful.":
        "أن نصل بالعلامة المناسبة إلى الصوت المناسب.",
    "To empower brands with tailored influencer marketing strategies that amplify their message and drive tangible results. We are committed to leveraging our decade-long expertise and global network to create impactful campaigns that resonate with audiences around the world.":
        "تمكين العلامات التجارية من خلال استراتيجيات تسويقية مخصصة للمؤثرين تعمل على تعزيز رسالتهم وتحقيق نتائج ملموسة. نحن ملتزمون بالاستفادة من خبرتنا الممتدة لعقد من الزمان وشبكتنا العالمية لإنشاء حملات مؤثرة تلقى صدى لدى الجماهير في جميع أنحاء العالم.",
    "What sets us apart":
        "ما نقوم عليه",
    "Exceptional strategies.": "استراتيجيات استثنائية.",
    "At Elite, we understand that exceptional results require exceptional strategies. That's why we've spent over 10 years cultivating relationships with elite influencers and high-end brands, ensuring that our clients have access to the best talent and opportunities across the globe — bespoke campaigns that transcend borders and resonate with diverse audiences.":
        "في Elite، ندرك أن النتائج الاستثنائية تتطلب استراتيجيات استثنائية. ولهذا السبب أمضينا أكثر من 10 سنوات في تنمية العلاقات مع المؤثرين النخبة والعلامات التجارية الراقية، لضمان حصول عملائنا على أفضل المواهب والفرص في جميع أنحاء العالم. تمكننا خبرتنا الواسعة وبصمتنا الدولية من تصميم حملات مخصصة تتجاوز الحدود وتتردد صداها مع جماهير متنوعة.",
    "Why choose Elite": "لماذا تختار Elite",
    "Five reasons brands stay.":
        "خمسة أمور لا نساوم عليها.",
    "Decade of excellence": "عقد من التميز",
    "With over 10 years of experience in the industry, GC Elite brings a wealth of knowledge and expertise to every campaign we undertake.":
        "مع أكثر من 10 سنوات من الخبرة في الصناعة، تجلب GC Elite ثروة من المعرفة والخبرة لكل حملة نقوم بها.",
    "Our presence in over 52 countries enables us to connect brands with influencers and audiences on a global scale, ensuring maximum reach and impact.":
        "يتيح لنا وجودنا في أكثر من 52 دولة ربط العلامات التجارية بالمؤثرين والجماهير على نطاق عالمي، مما يضمن أقصى قدر من الوصول والتأثير.",
    "We pride ourselves on our exclusive partnerships with high-end brands and elite influencers, ensuring that our clients have access to the best talent and opportunities worldwide.":
        "نفخر بشراكاتنا الحصرية مع العلامات التجارية الراقية والمؤثرين النخبويين، مما يضمن حصول عملائنا على أفضل المواهب والفرص في جميع أنحاء العالم.",
    "We're committed to delivering measurable results that drive real business growth and ROI for our clients, no matter where they are in the world.":
        "نحن ملتزمون بتقديم نتائج قابلة للقياس تدفع النمو التجاري الحقيقي وعائد الاستثمار لعملائنا، بغض النظر عن مكان وجودهم في العالم.",
    "Exceptional quality": "الجودة الاستثنائية",
    "From campaign conception to execution, we maintain the highest standards of quality and professionalism in everything we do.":
        "من تصور الحملة إلى التنفيذ، نحافظ على أعلى معايير الجودة والاحتراف في كل ما نقوم به.",
    "Let's talk about your next campaign.":
        "أخبرنا بما تريد إطلاقه.",
    "Ready to elevate your brand with the power of influencer marketing on a global scale? Get in touch today to learn more about our services and how we can help you achieve your marketing goals.":
        "سنعود إليك بصنّاع المحتوى والخطة والأرقام. عادةً خلال يومين.",
    "Thanks — an Elite partner manager will be in touch.":
        "شكرًا لك — سنتواصل معك قريبًا.",
    "Thanks — we'll reply with a campaign outline shortly.":
        "شكرًا لك — سنتواصل معك قريبًا.",
    "You're subscribed. Welcome to Elite.":
        "تم اشتراكك. أهلًا بك في إيليت.",
    "Niche Mastery Redefined":
        "إتقانٌ يُعيد تعريف التميّز",
    "Follower reach":
        "متابع نصل إليهم",
    "Featured clients":
        "عملاء مختارون",
    "Restaurants, fashion houses and beauty brands across the Gulf and beyond.":
        "مطاعم ودور أزياء وعلامات تجميل في الخليج وخارجه.",
}


# Elements carrying data-tr use this map instead of their English text, so a word
# that means one thing on a service card and another in a form is not forced to
# share a translation.
# Per-campaign media alt text, generated from case_studies.WITH_MEDIA.
AR.update({
    "Black Tap campaign still": "لقطة من حملة Black Tap",
    "Sobhy Kaber campaign still": "لقطة من حملة Sobhy Kaber",
    "Mr.Chow campaign still": "لقطة من حملة Mr.Chow",
    "Jon & Vinny's campaign still": "لقطة من حملة Jon & Vinny's",
    "Crazy Pizza campaign still": "لقطة من حملة Crazy Pizza",
    "A.O.K Kitchen campaign still": "لقطة من حملة A.O.K Kitchen",
    "Nawader Aloud campaign still": "لقطة من حملة Nawader Aloud",
    "Beefbar campaign still": "لقطة من حملة Beefbar",
    "Enigmaku campaign film": "فيلم حملة Enigmaku",
    "Play the Enigmaku film": "تشغيل فيلم Enigmaku",
    "Rüya campaign still": "لقطة من حملة Rüya",
    "tabl.to campaign film": "فيلم حملة tabl.to",
    "Play the tabl.to film": "تشغيل فيلم tabl.to",
    "KAYZŌ campaign still": "لقطة من حملة KAYZŌ",
    "Tashas Cafe campaign film": "فيلم حملة Tashas Cafe",
    "Play the Tashas Cafe film": "تشغيل فيلم Tashas Cafe",
    "Iris campaign still": "لقطة من حملة Iris",
    "Clap campaign still": "لقطة من حملة Clap",
    "Brute campaign still": "لقطة من حملة Brute",
    "Lavenue campaign still": "لقطة من حملة Lavenue",
    "Beit El Sabban campaign film": "فيلم حملة Beit El Sabban",
    "Play the Beit El Sabban film": "تشغيل فيلم Beit El Sabban",
    "Jones the Grocer campaign film": "فيلم حملة Jones the Grocer",
    "Play the Jones the Grocer film": "تشغيل فيلم Jones the Grocer",
    "Urth Caffe campaign still": "لقطة من حملة Urth Caffe",
    "Zuma campaign still": "لقطة من حملة Zuma",
    "ROKA KSA campaign still": "لقطة من حملة ROKA KSA",
    "Il Baretto campaign still": "لقطة من حملة Il Baretto",
    "MYAZŪ campaign still": "لقطة من حملة MYAZŪ",
    "Agio campaign still": "لقطة من حملة Agio",
    "Maserati campaign still": "لقطة من حملة Maserati",
    "Kiko campaign film": "فيلم حملة Kiko",
    "Play the Kiko film": "تشغيل فيلم Kiko",
    "St. Regis Hotels campaign still": "لقطة من حملة St. Regis Hotels",
    "Million Riyal Menu campaign film": "فيلم حملة Million Riyal Menu",
    "Play the Million Riyal Menu film": "تشغيل فيلم Million Riyal Menu",
    "Panerai campaign still": "لقطة من حملة Panerai",
    "Fred campaign still": "لقطة من حملة Fred",
    "Gia campaign still": "لقطة من حملة Gia",
    "Rituals Cosmetics campaign film": "فيلم حملة Rituals Cosmetics",
    "Play the Rituals Cosmetics film": "تشغيل فيلم Rituals Cosmetics",
    "The Back Burner campaign still": "لقطة من حملة The Back Burner",
})

# Film-reel strings, generated from case_studies.WITH_MEDIA.
AR.update({
    "Creators": "صنّاع المحتوى",
    "The films.": "الأفلام.",
    "« Featured work »": "« أعمال مختارة »",
    '12M REACH // 118 CREATORS': '12M وصول // 118 صانع محتوى',
    '13.9M REACH // 58 CREATORS': '13.9M وصول // 58 صانع محتوى',
    '17.9M REACH // 87 CREATORS': '17.9M وصول // 87 صانع محتوى',
    '19.7M REACH // 360 CREATORS': '19.7M وصول // 360 صانع محتوى',
    '2.1M REACH // 1 CREATOR': '2.1M وصول // صانع محتوى واحد',
    '24.9M REACH // 186 CREATORS': '24.9M وصول // 186 صانع محتوى',
    '571.5K REACH // 8 CREATORS': '571.5K وصول // 8 صنّاع محتوى',
    '58 creators in Saudi Arabia, reaching a combined 13.9M followers.': '58 صانع محتوى في السعودية، بوصول تراكمي إلى 13.9M متابع.',
    '87 creators in Saudi Arabia, reaching a combined 17.9M followers.': '87 صانع محتوى في السعودية، بوصول تراكمي إلى 17.9M متابع.',
    '98.5K REACH // 2 CREATORS': '98.5K وصول // صانعَي محتوى',
    'A focused group of 2 creators in Saudi Arabia, reaching a combined 98.5K followers.': 'مجموعة مركّزة من صانعَي محتوى في السعودية، بوصول تراكمي إلى 98.5K متابع.',
    'A focused group of 8 creators in Saudi Arabia, reaching a combined 571.5K followers.': 'مجموعة مركّزة من 8 صنّاع محتوى في السعودية، بوصول تراكمي إلى 571.5K متابع.',
    'A network of 118 creators in Saudi Arabia, reaching a combined 12M followers.': 'شبكة من 118 صانع محتوى في السعودية، بوصول تراكمي إلى 12M متابع.',
    'A network of 186 creators in Kuwait, reaching a combined 24.9M followers.': 'شبكة من 186 صانع محتوى في الكويت، بوصول تراكمي إلى 24.9M متابع.',
    'A network of 360 creators in Saudi Arabia, reaching a combined 19.7M followers.': 'شبكة من 360 صانع محتوى في السعودية، بوصول تراكمي إلى 19.7M متابع.',
    'A single creator in Saudi Arabia, reaching 2.1M followers.': 'صانع محتوى واحد في السعودية، بوصول إلى 2.1M متابع.',
    'Kuwait // Fashion & accessories': 'الكويت // أزياء وإكسسوارات',
    'Saudi Arabia // Beauty': 'السعودية // تجميل',
    'Saudi Arabia // Cafe': 'السعودية // مقاهٍ',
    'Saudi Arabia // Restaurant': 'السعودية // مطاعم',
    'Saudi Arabia': 'السعودية',
})

AR_KEYED = {
    "svc.01.top": "اكتشاف",
    "svc.01.bottom": "المؤثرين",
    "svc.02.top": "استراتيجية",
    "svc.02.bottom": "الحملة",
    "svc.03.top": "صناعة",
    "svc.03.bottom": "المحتوى",
    "svc.04.top": "تتبّع",
    "svc.04.bottom": "الأداء",
    "who.creator": "أنا صانع محتوى",
    "who.brand": "أنا علامة تجارية",
}
