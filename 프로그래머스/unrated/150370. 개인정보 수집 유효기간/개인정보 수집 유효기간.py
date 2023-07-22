def solution(today, terms, privacies):
    from datetime import datetime, timedelta

    def get_term(term_str):
        term, duration = term_str.split()
        return term, int(duration)

    def get_privacy(privacy_str):
        date_str, term = privacy_str.split()
        date = datetime.strptime(date_str, '%Y.%m.%d')
        return date, term

    def get_expiration_date(date, duration):
        year = date.year + duration // 12
        month = date.month + duration % 12
        if month > 12:
            year += 1
            month -= 12
        day = min(date.day, 28)
        expiration_date = datetime(year, month, day)
        return expiration_date - timedelta(days=1)

    today_date = datetime.strptime(today, '%Y.%m.%d')
    terms_dict = dict(get_term(term_str) for term_str in terms)
    result = []
    for i, privacy_str in enumerate(privacies):
        date, term = get_privacy(privacy_str)
        duration = terms_dict[term]
        expiration_date = get_expiration_date(date, duration)
        if today_date > expiration_date:
            result.append(i + 1)
    return result
