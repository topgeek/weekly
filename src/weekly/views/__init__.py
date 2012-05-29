from pyramid.view import view_config


@view_config(route_name='index', renderer='index.html')
@view_config(route_name='thankyou', renderer='thankyou.html')
def static_view(request):
    return {}


@view_config(route_name='subscribe', request_method='POST', renderer='json')
def subscribe(request):
    mc = request.registry['mc']
    data = request.POST
    if mc.listSubscribe(id=data['list_id'], email_address=data['email']):
        return {'status': 'success'}
    else:
        return {'status': 'failed'}
