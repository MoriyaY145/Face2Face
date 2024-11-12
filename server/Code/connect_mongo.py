import pymongo
client = pymongo.MongoClient("mongodb+srv://moriya0556796269:iRBJbjSB9Ywk6SGz@cluster0.wnesgpm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


db = client["face2fateHeb"]
col = db["face_regions"]
dict = ([
        {
            "name": "גבות",
            "features": [
                {
                    "name": "ישרות",
                    "analysis": "בעל יושר, כנה, רגיש, חביב, יצירתי ובעל קסם אישי."


                },
                {
                    "name": "קשתיות",
                    "analysis": "שאפתן, חסר סבלנות, בעל תכונות מנהיגות, דרמטי, נהנה מלהיות במרכז תשומת הלב, אמיץ, לא מפחד מקשיים. אבל לפעמים עלול להיות עקשן. "
                },
                {
                    "name": "מעגליות",
                    "analysis": "מתון, אדיב, ידידותי ותמיד חושב על הצרכים של אחרים. כשאתה מקבל החלטה, היא תתבסס על מה שאתה רוצה ועל מה שכולם עשויים לרצות לנסות, מה שיביא לניצחון כולם."
                }
            ]
        },
        {
            "name": "עיניים",
            "features": [
                {
                    "name": "קטנות",
                    "analysis": "מופנם, שכלי, בעל יכולת העמקה וריכוז, לא מושפע בקלות מאחרים ובדרך כלל אתה שמח בחלקך."
                },
                {
                    "name": "מוארכות",
                    "analysis": "בעל מראה טוב, מנת אינטליגנציה גבוהה יותר."
                },
                {
                    "name": "גדולות",
                    "analysis": "מוחצן, חברותי, בעל ביטחון עצמי. סקרן ויש לך יכולת קליטה מהירה."
                }
            ]
        },
        {
            "name": "פנים",
            "features": [
                {
                    "name": "משולשות",
                    "analysis": "מוחצן, אסטרטיבי, חברתי ונהנה להיות אחראי. יצירתי ואמנותי אך נוטה לכיוון של חוסר סבלנות.אתה נוטה להצליח מאד בשל האופי הנחרץ שלך."
                },
                {
                    "name": "סגלגליות",
                    "analysis": " מתודי, שאפתן, מעשי, בעל הישגים גבוהים, לא אוהב נורמות של חברה ושגרה ארצית, שילוב של מופנמות ומוחצנות, טוב בלהרגיש טוב לאחרים."
                },
                {
                    "name": "מרובעות",
                    "analysis": "חזק, פעיל מאד, אנרגטי, אנליטי, מהיר שכל, פרואקטיבי, רגוע במצבי לחץ, מנהיג ומקבל החלטות טובות."
                },
                {
                    "name": "מעגליות",
                    "analysis": "אדיב, ידידותי ואוהד, בדרך כלל בקשר טוב עם אחרים, נתינה (לעיתים נותן יתר על המידה), רחמן, נוח, סובלני וטוב ביחסים בין אישיים."
                }
            ]
        },
        {
            "name": "פה",
            "features": [
                {
                    "name": "קטן",
                    "analysis": "אישיות יותר מופנמת ושמרנית. לעתים קרובות אתה אובד עצות כאשר אתה נתקל בקשיים."
                },
                {
                    "name": "בינוני",
                    "analysis": "מערכת יחסים טובה עם אחרים ואתה די פופולרי. יש לך מזל גם לקריירה וגם לעושר."
                },
                {
                    "name": "עבה",
                    "analysis": "נלהב וחם לב, עושה דברים מעשיים וממורמרים, ופחות משתמש בתחבולות."
                }
            ]
        },
        {
            "name": "אף",
            "features": [
                {
                    "name": "רחב",
                    "analysis": "החלטי, נמרץ, ובעל אומץ וכישרון. טוב נפש ומוכן לעבוד קשה, אבל עם הערכה עצמית חזקה ועוצמה ניכרת, לא תחסך במאמץ במרדף אחר עושר."
                },
                {
                    "name": "ארוך",
                    "analysis": "בעל כישורי חשיבה מעמיקים, אך לעתים קרובות חושב יותר ומהסס. לא אוהב לבטוח במוחך. יש לך מגוון רחב של תחומי עניין אבל אתה שמרני, יציב ובודד."
                },
                {
                    "name": "קטן",
                    "analysis": "מתחשב ורגיש בעל אישיות שמרנית ושלווה. אתה בדרך כלל מתגלה כחמוד, עליז ומלא חיבה."
                }
            ]
        }
    ])

col.insert_many(dict)