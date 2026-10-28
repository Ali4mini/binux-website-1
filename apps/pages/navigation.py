"""Bilingual navigation groups using the reference's tabbed preview structure."""
from .content import SERVICES


def navigation(lang):
    fa = lang == 'fa'
    def text(en, persian): return persian if fa else en
    def item(title, slug, description=''):
        return {'title': title, 'slug': slug, 'description': description}
    def group(key, en, persian, icon, rows, tone='lilac'):
        return {'key': key, 'title': text(en, persian), 'icon': icon, 'items': rows, 'tone': tone}
    services = {s['slug']: s[lang] for s in SERVICES}
    def link(slug): return item(services[slug]['title'], slug, services[slug]['description'])
    groups = [
        group('product', 'Product Engineering', 'مهندسی محصول', 'spark', [link('custom-software'), link('crm-erp'), link('bots-automation'), link('ai-assisted-engineering')]),
        group('crm', 'CRM Engineering', 'مهندسی CRM', 'system', [item(text('Custom CRM Development','توسعه CRM اختصاصی'),'crm-erp',text('Customer workflows shaped around your business.','فرایندهای مشتری متناسب با کسب‌وکار شما.')),item(text('CRM Integration','یکپارچه‌سازی CRM'),'crm-erp',text('Connect customer information to the tools you use.','اطلاعات مشتری را به ابزارهای فعلی متصل کنید.')),item(text('CRM for Real Estate','CRM برای املاک'),'crm-erp',text('Property and customer workflows in one place.','فرایندهای ملک و مشتری در یک محیط.')),item(text('Customer Workflow Automation','اتوماسیون فرایندهای مشتری'),'bots-automation',text('Make repetitive customer handoffs manageable.','جابه‌جایی‌های تکراری اطلاعات مشتری را مدیریت کنید.'))]),
        group('erp', 'ERP Engineering', 'مهندسی ERP', 'erp', [item(text('Custom ERP Development','توسعه ERP اختصاصی'),'crm-erp',text('Business operations connected in one system.','عملیات کسب‌وکار در یک سامانه یکپارچه.')),item(text('Operational Dashboards','داشبوردهای عملیاتی'),'custom-software',text('A clear view of your team’s day-to-day work.','دیدی روشن از کارهای روزمره تیم.')),item(text('ERP Integration','یکپارچه‌سازی ERP'),'crm-erp',text('Connect the tools behind your operations.','ابزارهای عملیاتی کسب‌وکار را به هم وصل کنید.')),item(text('Team Workflows & Access','فرایندها و دسترسی‌های تیم'),'crm-erp',text('Roles, permissions and practical handoffs.','نقش‌ها، دسترسی‌ها و تحویل کار میان افراد.'))]),
        group('web-mobile', 'Web & Mobile', 'وب و موبایل', 'mobile', [link('mobile-apps'),item(text('Cross-Platform Experiences','تجربه چندسکویی'),'mobile-apps',text('Connected web and mobile product workflows.','فرایندهای یکپارچه محصول در وب و موبایل.')),item(text('Web App Development','توسعه وب‌اپلیکیشن'),'web-development',text('Maintainable applications built around your users.','برنامه‌های قابل نگهداری متناسب با کاربران.')),link('web-development'),item(text('Backend Development','توسعه بک‌اند'),'custom-software',text('APIs, databases and Python services.','API، پایگاه داده و سرویس‌های پایتون.')),item(text('Business Websites','وب‌سایت کسب‌وکار'),'web-development',text('Responsive websites and online stores.','وب‌سایت‌های واکنش‌گرا و فروشگاه اینترنتی.'))]),
        group('design', 'Design & Experience', 'طراحی و تجربه', 'web', [item(text('Responsive Web Experiences','تجربه واکنش‌گرای وب'),'web-development',text('Your product across desktop and mobile screens.','محصول شما در نمایشگرهای دسکتاپ و موبایل.')),item(text('Mobile Product Experience','تجربه محصول موبایل'),'mobile-apps',text('Interfaces connected to your product workflows.','رابط کاربری هماهنگ با فرایندهای محصول.')),item(text('Management Interfaces','رابط‌های مدیریتی'),'custom-software',text('Clear dashboards for everyday operations.','داشبورد روشن برای کارهای روزمره.'))]),
        group('launch', 'Launch & Growth', 'شروع و توسعه', 'rocket', [item(text('First Product Release','اولین نسخه محصول'),'custom-software',text('Define and build the first useful version.','اولین نسخه مفید را تعریف و پیاده‌سازی کنید.')),item(text('Product Integrations','یکپارچه‌سازی محصول'),'bots-automation',text('Connect your product to the services it needs.','محصول را به سرویس‌های موردنیاز متصل کنید.')),item(text('Website Development','توسعه وب‌سایت'),'web-development',text('Build the web presence behind your business.','حضور آنلاین کسب‌وکار را بسازید.'))]),
        group('quality', 'Quality & Support', 'کیفیت و پشتیبانی', 'check', [item(text('Code Review & Testing','بازبینی کد و آزمون'),'ai-assisted-engineering',text('Engineering checks throughout implementation.','بررسی‌های مهندسی در مسیر پیاده‌سازی.')),item(text('Application Maintenance','نگهداری نرم‌افزار'),'custom-software',text('A defined scope for the product you already have.','محدوده‌ای مشخص برای محصول فعلی شما.')),item(text('Technical Handover','تحویل فنی'),'custom-software',text('Deployment preparation and project documentation.','آماده‌سازی استقرار و مستندات پروژه.'))]),
        group('team', 'Work With Our Team', 'همکاری با تیم ما', 'team', [link('custom-software'),link('web-development'),link('mobile-apps')]),
    ]
    crm_groups = [
        ('Custom CRM Development','توسعه CRM اختصاصی'), ('CRM Workflow Planning','برنامه‌ریزی فرایندهای CRM'),
        ('CRM Integration','یکپارچه‌سازی CRM'), ('CRM Migration Planning','برنامه‌ریزی انتقال CRM'),
        ('Customer Workflow Automation','اتوماسیون فرایندهای مشتری'), ('Mobile CRM Interfaces','رابط موبایل CRM'),
        ('Operational Dashboards','داشبوردهای عملیاتی'), ('Roles & Permissions','نقش‌ها و دسترسی‌ها'),
        ('CRM Maintenance','نگهداری CRM'),
    ]
    crm_workflows = [('Lead Management','مدیریت سرنخ'), ('Customer Organization','سازمان‌دهی مشتری'),
        ('Team Workflows','فرایندهای تیم'), ('Property Workflows','فرایندهای ملک'),
        ('Reporting Views','نماهای گزارش‌گیری'), ('Access Controls','کنترل دسترسی'),
        ('Service Handoffs','انتقال کارهای خدمات'), ('Mobile Access','دسترسی موبایل'), ('API Connections','اتصال به API')]
    crm = next(group for group in groups if group['key'] == 'crm')
    crm['left_items'] = [item(text(en,fa),'crm-erp') for en,fa in crm_groups]
    crm['right_items'] = [item(text(en,fa),'crm-erp') for en,fa in crm_workflows]
    crm['left_heading'] = text('CRM SERVICES','خدمات CRM')
    crm['right_heading'] = text('CRM WORKFLOWS','فرایندهای CRM')
    crm['left_description'] = text('Build, integrate and organize customer workflows.','ساخت و یکپارچه‌سازی فرایندهای مشتری.')
    crm['right_description'] = text('Connected workflows for your business operations.','فرایندهای متصل برای عملیات کسب‌وکار.')
    crm['cta_title'] = text('Discuss Your CRM Requirements','درباره نیازهای CRM صحبت کنیم')
    crm['cta_description'] = text('Tell us which customer workflows your team needs to connect.','بگویید تیم شما به اتصال کدام فرایندهای مشتری نیاز دارد.')
    crm['cta_button'] = text('Discuss CRM','گفت‌وگو درباره CRM')
    ai = [group('assisted','AI-Assisted Delivery','توسعه با کمک هوش مصنوعی','spark',[link('ai-assisted-engineering'),item(text('Specification-Led Development','توسعه بر پایه شرح نیاز'),'ai-assisted-engineering',text('A clear scope before implementation begins.','محدوده روشن پیش از شروع پیاده‌سازی.')),item(text('Engineering Review','بازبینی مهندسی'),'ai-assisted-engineering',text('Engineers own architecture and release decisions.','مسئولیت معماری و انتشار با مهندسان است.'))], 'blue'),group('automation','Workflow Automation','اتوماسیون فرایندها','bot',[link('bots-automation'),link('custom-software')], 'blue')]
    industries = [group('business','Business Operations','عملیات کسب‌وکار','system',[link('crm-erp'),link('custom-software')],'mint'),group('property','Real Estate','املاک','web',[item(text('Real Estate CRM','CRM املاک'),'crm-erp',text('Property and customer workflows for your team.','فرایندهای ملک و مشتری برای تیم شما.')),link('web-development')],'mint'),group('service','Service Businesses','کسب‌وکارهای خدماتی','bot',[link('bots-automation'),link('mobile-apps')],'mint')]
    tech = [
      ('ai','AI-Assisted Dev Tools','ابزارهای توسعه با هوش مصنوعی',['Codex','Hermes','OpenCode','AI-assisted tools']),
      ('frontend','Frontend Development','توسعه فرانت‌اند',['React','JavaScript','TypeScript','React Native','Expo']),
      ('frontend-tools','Frontend Tools & Libraries','ابزارها و کتابخانه‌های فرانت‌اند',['Tailwind CSS','React Router','Vite']),
      ('backend','Backend Development','توسعه بک‌اند',['Python','Django','REST APIs']),
      ('database','Database','پایگاه داده',['PostgreSQL','Redis','SQLite']),
      ('cloud','Cloud & Deployment','ابر و استقرار',['Docker','Linux','Google Cloud']),
      ('automation','Automation','اتوماسیون',['Telegram','Python','REST APIs']),
      ('devops','DevOps','دوآپس',['GitHub Actions','Git','Docker','Linux']),
    ]
    logos = {name:'website/technology/'+slug+'.svg' for name,slug in [('React','react'),('React Native','react'),('JavaScript','javascript'),('TypeScript','typescript'),('Expo','expo'),('Tailwind CSS','tailwindcss'),('React Router','reactrouter'),('Vite','vite'),('Python','python'),('Django','django'),('PostgreSQL','postgresql'),('Redis','redis'),('SQLite','sqlite'),('Docker','docker'),('Linux','linux'),('Google Cloud','googlecloud'),('Telegram','telegram'),('GitHub Actions','githubactions'),('Git','git')]}
    return {'service_groups':groups, 'ai_groups':ai,'industry_groups':industries,
            'technology_groups':[{'key':key,'title':text(en,persian),'tools':[{'title':tool,'logo':logos.get(tool,'')} for tool in tools]} for key,en,persian,tools in tech],
            'nav_ai':text('AI','هوش مصنوعی'),'nav_industries':text('Industries','صنایع'),'nav_work':text('Case Studies','نمونه‌کارها'),'nav_quote':text('Pricing','برآورد'),
            'nav_view':text('View all services →','همه خدمات ←'),'nav_start':text('Start a Project','شروع پروژه'),
            'nav_note':text('Web, mobile & business software · Engineer-led delivery','وب، موبایل و نرم‌افزار کسب‌وکار · توسعه با مسئولیت مهندسان'),
            'nav_support':text('Clear scope · Direct communication · Technical handover','محدوده روشن · ارتباط مستقیم · تحویل فنی'),
            'nav_team':text('Meet the Team','آشنایی با تیم'),'nav_who':text('WHO WE ARE','درباره ما'),'nav_partner':text('WORK WITH US','همکاری با ما'),'nav_approach':text('OUR APPROACH','روش ما'),
            'nav_plan':text('Discuss Your Requirements','گفت‌وگو درباره نیازها'),'nav_about':text('About Us','درباره ما'),'nav_languages':text('Persian & English','فارسی و انگلیسی')}
