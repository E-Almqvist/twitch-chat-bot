from typing import Dict
from typing import Match


def optional_user_arg(match: Match[str]) -> str:
    _, _, rest = match['msg'].strip().partition(' ')
    if rest:
        return rest.lstrip('@')
    else:
        return match['user']


def parse_badge_info(s: str) -> Dict[str, str]:
    ret = {}
    for part in s.split(';'):
        k, v = part.split('=', 1)
        ret[k] = v
    return ret


def is_moderator(match: Match[str]) -> bool:
    info = parse_badge_info(match['info'])
    badges = info['badges'].split(',')
    return any(badge.startswith('moderator/') for badge in badges)
