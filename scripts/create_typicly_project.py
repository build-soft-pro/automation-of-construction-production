import pandas as pd

df = pd.read_excel(app.context_parameters.get('Файл'), 'Работы')

project = app.dictionary('Типовые проекты').create({
    'Код': app.context_parameters.get('Название')
})

for index, row in df.iterrows():
    app.dictionary('Работы типового проекта').create({
        'Типовой проект': project.id, 
        'Наименование': row['Название']
    })
    
app.notify(app.context_user, 'Типовой проект создан!')