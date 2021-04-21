import streamlit as st 
import pandas as pd 
import numpy as np 
#import matplotlib.pyplot as plt
from PIL import Image
import streamlit.components.v1 as components 

st.set_page_config(layout="wide")
def add_data(BBN,RT,HD,LF,LM,WM,WL,RLW,FE):
    c2.execute('INSERT INTO bdata(BBN,RT,HD,LF,LM,WM,WL,RLW,FE) VALUES (?,?,?,?,?,?,?,?,?)',(BBN,RT,HD,LF,LM,WM,WL,RLW,FE))
    conn2.commit()

pages = ["Home", "Tests","About tests",]
page = st.sidebar.radio("Menu Bar", options=pages)
if page == "Tests":
    st.write('General Information:')
    BBN = st.text_input(':نام و نام خانوداگی')
    col1, col2,col3,col4 =st.beta_columns(4)
    with col1:
        BBN = st.text_input(':سن')
    with col2:
        BBN = st.text_input(':تحصیلات')
    with col3:
        BBN = st.text_input(':وضعیت تاهل')
    with col4:
        BBN = st.text_input(':گروه خونی')

    st.write('Decision Styles:')
    options = ["خیلی زیاد", "زیاد", "متوسط", "کم","خیلی کم"]
    q1=st.selectbox(" من به زمان بندی در کارها اهمیت می دهم",options)
    q2=st.selectbox(" برای تصمیمات مهم اطلاعات کامل و صحیح را جمع آوری می کنم",options)
    q3=st.selectbox(" در مواقع رو به رو شدن با خطرات احتمالی و فشار زمانی موقعیت را به خوبی اداره می کنم",options)
    q4=st.selectbox("  نتایج و پیامدهای فعالیت هایم را مورد ارزیابی قرار می‌دهم",options)
    q5=st.selectbox("  داده های مورد نیاز فعالیت هایم را مورد ارزیابی قرار می‌دهم",options)
    q6=st.selectbox(" ایده های موجود را با روشی جدید و یا در قبال موقعیت های جدید به کار می‌گیرم",options)
    q7=st.selectbox(" نتایج و عملکرد نهائی کارها برایم اهمیت زیادی دارد",options)
    q8=st.selectbox(" در انجام کارها هم نتیجه و هم روش برایم اهمیت دارد",options)
    q9=st.selectbox(" غالباً در جستجو فرصت ها و زمینه های جدید انجام کار، ایجاد مدل‌های بدیع و روش های نو هستم",options)
    q10=st.selectbox("  برنامه های آموزشی باید بر مبنای اندازه گیری های دقیق، داده های صحیح، تجزیه و تحلیل کامل صورت گیرد",options)
    q11=st.selectbox("  مدیریت کارآمد باید همواره نظرات و پیشنهاد های کارکنان و پرسنل را مد نظر قرار دهد",options)
    q12=st.selectbox(" در دسترس بودن داده ها و اطلاعات برای پرسنل اهمیت بسیاری دارد",options)
    q13=st.selectbox(" مدیران باید همواره تغییرات را در محیط کار طراحی و تدوین کنند",options)
    q14=st.selectbox(" به نظر شما تحقیق به عنوان ابزار موثر ایجاد زمینه برای خلاقیت و نوآوری تا چه اندازه اهمیت دارد",options)
    q15=st.selectbox("  آیا به حمایت همکاران خود در کار اهمیت زیادی می دهید؟ ",options)
    q16=st.selectbox(" در محیط کاری، پاسخگوی نظرات همکاران، همترازان، رؤسا و ارباب رجوع به روش سازنده هستم",options)
    q17=st.selectbox(" در کارهای تیمی و مشارکتها اطلاعات ضروری را به طور مرتب به همه ارائه می کنم",options)
    q18=st.selectbox(" حقایق و مسائل کاری را به صورت مکتوب و سازماندهی شده ارائه می کنم",options)
    q19=st.selectbox(" جلسات را به روشی که امکان رسیدن به نتایج کاملا مشخص و روشن باشد، سازماندهی می کنم",options)
    q20=st.selectbox(" از نقطه نظراتم در مقابل دیگران به خوبی دفاع می کنم",options)
    q21=st.selectbox(" گزارشات شفاهی را به صورت صریح و روشن به افراد ارائه می کنم",options)
    q22=st.selectbox(" درصورت لزوم تصمیمات سخت می گیرم",options)
    q23=st.selectbox(" به هنگام عدم وجود اطلاعات (با اطلاعات ناقص) بهترین تصمیم ممکن را می گیرم",options)
    q24=st.selectbox(" در جلسات و مشورتهای کاری با مطرح کردن سوالات مختلف باعث می‌شوم که کارکنان ابعاد دیگر مسائل را ببیند",options)
    q25=st.selectbox("  تغییرات لازم را بر اساس اولویت به خوبی انجام می‌دهم",options)
    q26=st.selectbox("  در مواجه با موانع قابلیت تصمیم گیری منطقی را دارم",options)
    q27=st.selectbox("  همیشه به دنبال کشف زمینه های مشترک کاری در سازمان هستم",options)
    q28=st.selectbox(" بدون توجه به محدوده کاری خود به دنبال یافتن زمینه های مشترک کاری باذی نفعان هستم",options)
    q29=st.selectbox(" هنگام کار با گروهی که به تضاد و کشمکش می رسد با یافتن نظرات مشترک به انجام امور کمک می کنم",options)
    q30=st.selectbox(" در نوشتن و ارتباطات شفاهی و همچنین گوش دادن به آسودگی عمل می کنم",options)
    q31=st.selectbox(" من اقدام به هدفگزاری نموده و برای هر چیزی یک چشم انداز بلند مدت تعیین می کنم، تا همین امور را انجام دهند",options)
    q32=st.selectbox(" در برابر رخدادهای تصادفی تا سر حد رها کردن برنامه جاری خود، حساسیت و عکس العمل نشان می دهیم",options)
    q33=st.selectbox(" خطرات و شکست های احتمالی را مانعی برای طرح جدید و یا نظرات جدید نمی دانم",options)

    st.write('Thinking Styles:')
    options2 = ['کاملاً','بسیار زیاد','زیاد','تاحدودی','کم','بسیار کم','اصلاً']

    p1=st.selectbox(" هنگام رويارو شدن با يك مساله ،انديشه ها و روش هاي خودم را براي حل آن به كار مي برم",options2)
    p2=st.selectbox(" دوست دارم با افكارم بازي بكنم و ببينم آنها به چه چيزي منتهي مي شوند",options2)
    p3=st.selectbox(" مسائلي را دوست دارم که در آنها بتوانم راه حل هاي شخصي خودم را امتحان کنم",options2)
    p4=st.selectbox(" دوست دارم با افكار خودم ، كار را آغاز كنم",options2)
    p5=st.selectbox(" از موقعيت هايي كه فرصت استفاده از افكار و روش هاي خودم را دارم ، لذت مي برم",options2)
    p6=st.selectbox(" دوست دارم چگونگی حل یک مسئله بدنبال قوانين مشخص را بفهمم",options2)
    p7=st.selectbox(" دقت مي کنم که روش مناسبي را براي حل هر مسئله اي به کار ببرم",options2)
    p8=st.selectbox(" از کار کردن بر روي مسائلي که دستورالعمل مشخصي دارد، لذت مي برم",options2)
    p9=st.selectbox(" طرح هايي را دوست دارم كه ساختار روشني داشته و داراي برنامه و هدف مشخصي هستند",options2)
    p10=st.selectbox(" براي حل مشكل يا انجام دادن كار ، مايلم از دستورالعمل های مشخصي پيروي کنم",options2)
    p11=st.selectbox(" موقعيت هايي را دوست دارم که بتوانم روش هاي متفاوتِ انجام كارها را مقايسه و ارزیابی كنم",options2)
    p12=st.selectbox(" دوست دارم که نظرات متضاد و ديدگاه هاي متناقض را بررسي و ارزيابي کنم",options2)
    p13=st.selectbox(" طرح هايي را دوست دارم که بتوانم نظرات و ديدگاه هاي مختلف را مورد بررسي و ارزيابي قرار دهم",options2)
    p14=st.selectbox(" تکليف ها يا مسئله هايي را ترجيح مي دهم که بتوانم طرح ها يا روش های مورد استفادۀ ديگران را مورد ارزیابی قرار دهم",options2)
    p15=st.selectbox(" از كارهايي كه مستلزم تحليل، ارزيابي يا مقايسه اند ، لذت می برم ",options2)
    # model 1(all)
    datad = []
    datad.append([q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,q31,q32,q33])
    df = pd.DataFrame(datad,columns=('q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21','q22','q23','q24','q25','q26','q27','q28','q29','q30','q31','q32','q33'))
    df = df.replace(['خیلی زیاد'],'5')
    df = df.replace(['زیاد'],'4')
    df = df.replace(['متوسط'],'3')
    df = df.replace(['کم'],'2')
    df = df.replace(['خیلی کم'],'1')
    df = df.astype(int)
    #model 2 ( 1/2)
    dq12 = []
    dq12.append([q1,q2])
    dfq12 = pd.DataFrame(dq12, columns= ('q1','q2'))
    dfq12 = dfq12.replace(['خیلی زیاد'],'1')
    dfq12 = dfq12.replace(['زیاد'],'2')
    dfq12 = dfq12.replace(['متوسط'],'3')
    dfq12 = dfq12.replace(['کم'],'4')
    dfq12 = dfq12.replace(['خیلی کم'],'5')
    dfq12 = dfq12.astype(int)
    #model 3 (red 16/7/17)
    dm3 = []
    dm3.append([q16,q7,q17])
    dfm3 = pd.DataFrame(dm3, columns= ('q16','q7','q17'))
    dfm3 = dfm3.replace(['خیلی زیاد'],'4')
    dfm3 = dfm3.replace(['زیاد'],'5')
    dfm3 = dfm3.replace(['متوسط'],'3')
    dfm3 = dfm3.replace(['کم'],'2')
    dfm3 = dfm3.replace(['خیلی کم'],'1')
    dfm3 = dfm3.astype(int)
    #model 4 (blue 17/5/6)
    dm4 = []
    dm4.append([q17,q5,q6])
    dfm4 = pd.DataFrame(dm4, columns= ('q17','q5','q6'))
    dfm4 = dfm4.replace(['خیلی زیاد'],'3')
    dfm4 = dfm4.replace(['زیاد'],'4')
    dfm4 = dfm4.replace(['متوسط'],'5')
    dfm4 = dfm4.replace(['کم'],'2')
    dfm4 = dfm4.replace(['خیلی کم'],'1')
    dfm4 = dfm4.astype(int)
    #model 5 (23)
    dm5 = []
    dm5.append([q23])
    dfm5 = pd.DataFrame(dm5,columns = ['q23'])
    dfm5 = dfm5.replace(['خیلی زیاد'],'3')
    dfm5 = dfm5.replace(['زیاد'],'5')
    dfm5 = dfm5.replace(['متوسط'],'4')
    dfm5 = dfm5.replace(['کم'],'2')
    dfm5 = dfm5.replace(['خیلی کم'],'1')
    dfm5 = dfm5.astype(int)
    df['انعطاف پذیر'] = (dfm3['q16'] + dfm4['q17'] +dfm5['q23']+df['q24']+df['q28']+df['q29']+df['q1']+df['q8'])
    df['فراگیر'] = (dfq12['q1'] + df['q24'] +df['q10']+df['q11']+df['q2']+df['q3']+df['q5']+df['q16']+df['q17']+df['q27']+df['q31']+df['q12']+df['q14'])
    df['قاطع'] = (df['q4'] + dfm3['q7'] +df['q15']+df['q16']+df['q1']+dfq12['q2']+df['q23']+df['q22']+df['q13'])
    df['سلسله مراتبی'] = (df['q32'] + dfm4['q5'] +dfm3['q17']+dfm4['q6']+df['q20']+df['q16']+df['q7']+df['q8']+df['q30']+df['q31']+df['q12'])

    df['Total'] =  df['انعطاف پذیر'] + df['فراگیر'] + df['قاطع'] + df['سلسله مراتبی']  

    if st.button("Add "):
        
        st.write(df)
        if df.at[0,'سلسله مراتبی'] > 45:
            pic3 = Image.open('سلسه مراتبی-01-01.jpg')
            st.image(pic3, use_column_width=True)
        if df.at[0,'فراگیر'] > 45:
            pic4 = Image.open('فراگیر-01.jpg')
            st.image(pic4, use_column_width=True)
        if df.at[0,'قاطع'] > 35:
            pic5 = Image.open('قاطع-01.jpg')
            st.image(pic5, use_column_width=True)
        if df.at[0,'انعطاف پذیر'] > 30:
            pic6 = Image.open('انعطاف پذیر-01.jpg')
            st.image(pic6, use_column_width=True)
    ######################################################################################
        datat = []
        datat.append([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15])

        df2 = pd.DataFrame(datat,columns =('p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15'))
        df2 = df2.replace(['کاملاً'],'7')
        df2 = df2.replace(['بسیار زیاد'],'6')
        df2 = df2.replace(['زیاد'],'5')
        df2 = df2.replace(['تاحدودی'],'4')
        df2 = df2.replace(['کم'],'3')
        df2 = df2.replace(['بسیار کم'],'2')
        df2 = df2.replace(['اصلاً'],'1')
        df2 = df2.astype(int)

        df2['قانون گذار'] = (df2['p1'] + df2['p2'] + df2['p3'] + df2['p4'] + df2['p5'])
        df2['اجرایی محور'] = (df2['p6'] + df2['p7'] + df2['p8'] + df2['p9'] + df2['p10'])
        df2['قضاوت گر'] = (df2['p11'] + df2['p12'] + df2['p13'] + df2['p14'] + df2['p15'])
        df2new = pd.DataFrame(df2, columns = ['قانون گذار','اجرایی محور','قضاوت گر'])
        st.write(df2new)
        #df2['a'] = (df2['p1'] + df2['p2'] + df2['p3'] + df2['p4'] + df2['p5'])
        #df2['b'] = (df2['p6'] + df2['p7'] + df2['p8'] + df2['p9'] + df2['p10'])
        #df2['c'] = (df2['p11'] + df2['p12'] + df2['p13'] + df2['p14'] + df2['p15'])
        #df2new = pd.DataFrame(df2, columns = ['c','b','a'])
        #st.write(df2new)
        if (df2new.at[0,'قانون گذار'] > df2new.at[0,'اجرایی محور']) and (df2new.at[0,'قانون گذار'] > df2new.at[0,'قضاوت گر']):
            st.write("ghanon gozar")
        elif (df2new.at[0,'قانون گذار'] < df2new.at[0,'اجرایی محور']) and (df2new.at[0,'قضاوت گر'] < df2new.at[0,'اجرایی محور']):
            st.write("executive")
        else :
            st.write("judge")

elif page == "Home":

    st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;font-family:"B mitra", serif; color: blue;text-align: right;
    }
    </style> <p class="big-font">شرکت بهین راهبرد انفجار-واحد آموزش و نیروی انسانی</p>
    """, unsafe_allow_html=True)
    
    pic = Image.open('Hr.jpg')
    st.image(pic, use_column_width=True)
    pi = Image.open('p.jpg')
    st.image(pi, use_column_width=True)
    #st.title('بهترین راه برای ساختن سازمانی که برازنده آینده باشد، ساختن سازمانی است که برازنده انسان باشد')
    #st.write('گری همل')

    st.markdown("""
    <style>
    .big-font {
        font-size:40px !important;font-family:"B mitra", serif; color: blue;text-align: center;
    }
    </style><p class="big-font">.بهترین راه برای ساختن سازمانی که برازنده آینده باشد، ساختن سازمانی است که برازنده انسان باشد</p>
    """, unsafe_allow_html=True)
    #st.markdown('<p class="big-font">.بهترین راه برای ساختن سازمانی که برازنده آینده باشد، ساختن سازمانی است که برازنده انسان باشد</p>', unsafe_allow_html=True)

    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;font-family:"B mitra", serif;
    }
    </style>'<p class="big-font">"گری همل"</p>'
    """, unsafe_allow_html=True)
    #st.markdown('<p class="big-font">"گری همل"</p>', unsafe_allow_html=True)


elif page == "About tests":
    st.header("test html import")
    HtmlFile = open("test.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code)
    st.markdown(source_code, unsafe_allow_html=True) 
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;font-family:"B mitra", serif;direction: rtl;text-align: justify;
    }
    </style>'<p class="big-font">"هر سازمانی هم به افراد قانون‌گذار و هم به افراد قضاوت‌گر و هم به افراد مجری نیاز دارد. به هر حال در هر سازمانی بعضی از افراد یا گروه‌ها باید فرم‌ها را طراحی و برنامه‌ریزی کنند، بعضی آن‌ها را اجرا نمایند و گروهی دیگر باید سازمان را مطمئن کنند که تمام برنامه‌ها و فعالیت‌ها به خوبی پیش می‌رود. هیچ یک از این سبک‌ها بهتر یا بدتر از دیگری نیست بلکه نکته قابل توجه این است که هیچ سازمانی بدون تمام این سبک‌ها نمی‌تواند برای مدت طولانی دوام داشته باشد. هر سازمانی بدون افراد قانون‌گذار به اجبار مقلد سازمان‌های دیگر بوده و پشت سر آن‌ها قرار می‌گیرد، بدون افراد مجری برنامه‌های زیادی بدون اجرا در دست خواهد داشت و بدون افراد قضاوت‌گر موفق به ارزیابی صحیح سیاست‌ها و برنامه‌های اثر بخش و غیر اثر بخش خود نخواهد شد"</p>'
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;font-family:"B mitra", serif;direction: rtl;text-align: justify;
    }
    </style>'<p class="big-font">"دو جنبه از تصمیم‌گیری، بیشترین سهم را در تشریح و توصیف تفاوت‌های کلیدی در سبک‌های تصمیم‌گیری فراهم می‌کنند. آنها عبارتند از:۱) به کارگیری و استفاده از اطلاعات : مقداری از اطلاعات که در حقیقت برای تصمیم‌گیری مد نظر قرار می‌گیرند.          ۲) تمرکز: تعداد گزینه های مشخص حین رسیدن به تصمیمات."</p>""", unsafe_allow_html=True)
