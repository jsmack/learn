import re

RE_STACK_ID = re.compile(r"""
     arn:aws:cloudformation:
     (?P<region>[\w-]+):      # region
     (?P<account_id>[\d]+)   # account_id
     :stack/
     (?P<stack_name>[\w-]+)/  # stack_name
     [\w-]+""", re.VERBOSE)


RE_STACK_ID0 = re.compile(r'arn:aws:cloudformation:(?P<region>[\w-]+):(?P<account_id>[\d]+)'
               r':stack/(?P<stack_name>[\w-]+)/[\w-]+')

s1 = ('arn:aws:cloudformation:us-east-2:123456789012:stack/'
     'mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786')
s2 = ('arn:aws:cloudformation:us-east-2:123456789012:stack/'
     'mystack-mynestedstack-sggfrhxhuRaaaam7w/f449b250-b969-11e0-a185-5081d0136786')

for s in [s1, s2]:
     # m = re.match(r'arn:aws:cloudformation:(?P<region>[\w-]+):(?P<account_id>[\d]+)'
     #              r':stack/(?P<stack_name>[\w-]+)/[\w-]+', s)
     m = RE_STACK_ID.match(s)
     if m:
          #print(m)
          #print(m.span())
          #print(m.group())
          print(m.group('region'))
          print(m.group('account_id'))
          print(m.group('stack_name'))
     else:
          raise Exception('Error!')
