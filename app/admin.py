# from flask_admin.contrib.sqla import ModelView
# from wtforms.fields import SelectField  # Make sure to import this

# class CustomModelView(ModelView):
#     column_searchable_list = ['tracking_number', 'status', 'last_location']
#     can_create = True
#     can_edit = True
#     can_delete = True
#     page_size = 50

#     # Optional: reorder fields
#     form_columns = ['tracking_number', 'status', 'last_location', 'eta']

#     # Change labels
#     form_args = {
#         'tracking_number': {'label': 'Tracking Number'},
#         'status': {'label': 'Delivery Status'},
#         'last_location': {'label': 'Last Known Location'},
#         'eta': {'label': 'Estimated Arrival'}
#     }

#     # Use dropdown for status
#     form_overrides = {
#         'status': SelectField
#     }

#     form_args['status']['choices'] = [
#         ('pending', 'Pending'),
#         ('in_transit', 'In Transit'),
#         ('delivered', 'Delivered'),
#         ('delayed', 'Delayed')
#     ]


# from flask_admin.contrib.sqla import ModelView
# from wtforms.fields import SelectField

# class CustomModelView(ModelView):
#     column_searchable_list = ['tracking_number', 'status', 'last_location']
#     can_create = True
#     can_edit = True
#     can_delete = True
#     page_size = 50

#     form_overrides = {
#         'status': SelectField
#     }

#     form_args = {
#         'status': {
#             'choices': [
#                 ('In Transit', 'In Transit'),
#                 ('Delivered', 'Delivered'),
#                 ('Delayed', 'Delayed')
#             ]
#         }
#     }

from flask_admin.contrib.sqla import ModelView
from wtforms.validators import DataRequired
from .models import PackageTracking

class CustomModelView(ModelView):
    form_args = {
        'tracking_number': dict(
            label='Tracking Number',
            validators=[DataRequired()]
        ),
        'status': dict(
            label='Delivery Status',
            validators=[DataRequired()]
        ),
        'last_location': dict(
            label='Last Known Location'
        ),
        'eta': dict(
            label='Estimated Time of Arrival'
        )
    }

    column_searchable_list = ['tracking_number', 'status', 'last_location']
    column_filters = ['status']
    column_list = ['tracking_number', 'status', 'last_location', 'eta']
    can_export = True
