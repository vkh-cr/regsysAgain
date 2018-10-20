

def pair_payments(request):
    # TODO parametrize by time period (eg last day)
    statement_json = p.download_statement_json()
    ps = p.json_to_payments(statement_json)
    ps.save()

    for pay in ps:
        p.process_payment(pay)

def cancel_timed_out_payments(request):
    # TODO check this condition is consistent with date in thank_you msg (reg. confirmation email)
    older_then = datetime.now() - timedelta(days=14)
    for reg in DetailRegistrations.objects.filter(date_created <= older_then):
        reg.status = RegStatus.EXPIRED
        reg.save()

