import os
import re

directories = [
    '/home/leonardobarbosa/dev//app/repositories',
    '/home/leonardobarbosa/dev//sql/faturamento',
    '/home/leonardobarbosa/dev//docs/faturamento',
]

pattern1 = re.compile(
    r'(?i)case\s+when\s+cab\.codtipoper\s*=\s*3230\s+then\s+cab\.BASEISS\s+'
    r'when\s+cab\.codtipoper\s*=\s*3232\s+then\s+cab\.BASEISS\s+'
    r'else\s+cab\.vlrnota\s+end'
)
repl1 = "CASE WHEN ISNULL(CAB.AD_VLRFATMES,0) <> 0 THEN CAB.AD_VLRFATMES WHEN CAB.CODTIPOPER = 3230 THEN CAB.BASEISS WHEN CAB.CODTIPOPER = 3232 THEN CAB.BASEISS ELSE CAB.VLRNOTA END"

pattern2 = re.compile(
    r'(?i)case\s+when\s+codtipoper\s*=\s*3230\s+then\s+BASEISS\s+'
    r'when\s+codtipoper\s*=\s*3232\s+then\s+BASEISS\s+'
    r'else\s+vlrnota\s+end(\s+as\s+vlrnota)?'
)
repl2 = "vlrnota"

for directory in directories:
    for root, _, files in os.walk(directory):
        for file in files:
            if not file.endswith(('.py', '.sql', '.txt', '.md')):
                continue
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = pattern1.sub(repl1, content)
            new_content = pattern2.sub(repl2, new_content)

            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {path}")

