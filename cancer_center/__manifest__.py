{
    'name': 'cancer_center',
    'version': '1.0',
    'description': '',
    'category': 'custom_modules/anti cancer center',
    'depends': [
        'base'
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/protocol_view.xml',
        'views/medication_view.xml',
        'views/patient_view.xml',
        'views/protocol_assignment.xml',
        'views/protocol_assignment_detail.xml',
        'views/cure_view.xml',
        'views/reaction_view.xml',
        'views/cure_statistics_view.xml',
        'views/cancer_center_menus.xml'
    ],
    
    'assets': {
        'web.assets_backend':[
            'cancer_center/static/src/components/statView/statsView.js',
            'cancer_center/static/src/components/statView/statsView.xml',
            'cancer_center/static/src/components/statView/statsView.css',
        ]

    },
    'application': True
}

