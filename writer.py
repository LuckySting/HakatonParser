import json

file = open('result.xml', 'w', encoding='utf8')
data_f = open('hacks.json', 'rb')
data = json.load(data_f)
data_f.close()
file.write("""<?xml version="1.0" encoding="UTF-8"?>
<GLOSSARY>
  <INFO>
    <NAME>Профильные хакатоны</NAME>
    <INTRO>&lt;p&gt;Информация по собранным в результате работы профильные хакатоны.&lt;/p&gt;</INTRO>
    <INTROFORMAT>1</INTROFORMAT>
    <ALLOWDUPLICATEDENTRIES>0</ALLOWDUPLICATEDENTRIES>
    <DISPLAYFORMAT>dictionary</DISPLAYFORMAT>
    <SHOWSPECIAL>1</SHOWSPECIAL>
    <SHOWALPHABET>1</SHOWALPHABET>
    <SHOWALL>1</SHOWALL>
    <ALLOWCOMMENTS>0</ALLOWCOMMENTS>
    <USEDYNALINK>1</USEDYNALINK>
    <DEFAULTAPPROVAL>1</DEFAULTAPPROVAL>
    <GLOBALGLOSSARY>0</GLOBALGLOSSARY>
    <ENTBYPAGE>50</ENTBYPAGE>
    <ENTRIES>""")
for hack in data:
    file.write("""
    <ENTRY>
        <CONCEPT>{0}</CONCEPT>
        <DEFINITION>
        &lt;p&gt;&lt;strong&gt;Тема:&lt;/strong&gt;&lt;/p&gt;
          &lt;p&gt;{1}&lt;/p&gt;
        &lt;p&gt;&lt;strong&gt;Даты:&lt;/strong&gt;&lt;/p&gt;
              &lt;p&gt;{2}&lt;/p&gt;
        &lt;p&gt;&lt;strong&gt;Город:&lt;/strong&gt;&lt;/p&gt;
                  &lt;p&gt;{3}&lt;/p&gt;
        &lt;p&gt;&lt;strong&gt;Ссылка:&lt;/strong&gt;&lt;/p&gt;
                      &lt;p&gt;&lt;a href="{4}" data-mce-href="{4}"&gt;{4}&lt;/a&gt;&lt;/p&gt;
        </DEFINITION>
        <FORMAT>1</FORMAT>
        <USEDYNALINK>0</USEDYNALINK>
        <CASESENSITIVE>0</CASESENSITIVE>
        <FULLMATCH>0</FULLMATCH>
        <TEACHERENTRY>1</TEACHERENTRY>
      </ENTRY>
    """.format(hack['Название'], hack['Темы'], hack['Даты'], hack['Город'], hack['Ссылка']))
file.write("""
</ENTRIES>
  </INFO>
</GLOSSARY>
""")
file.close()
