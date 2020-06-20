def unpack_ipv6(ipv6_packed: list) -> None:

    """
    As you can see, this function unpacks ipv6, if it packed.
    Example: aaaa:: -> aaaa:0000:0000:0000:0000:0000:0000:0000
    """

    for i, ip in enumerate(ipv6_packed):
        splitted_ip = ip.split(':')
        if '' in splitted_ip:
            sliced_pre = splitted_ip[:splitted_ip.index('')]
            sliced_after = splitted_ip[splitted_ip.index('')+1:]
            while '' in sliced_pre:
                sliced_pre.remove('')
            while '' in sliced_after:
                sliced_after.remove('')
            range(8-len(sliced_pre+sliced_after))
            for _ in range(8-len(sliced_pre+sliced_after)):
                sliced_pre.append('0000')
            unpacked_value = ':'.join(sliced_pre + sliced_after)
            ipv6_packed[i] = unpacked_value


"""
Here are input ipv4/ipv6 lists
"""
ipv4_raw = [
    '64.231.132.104',
    '159.6.151.244',
    '225.112.60.158',
    '217.56.110.245',
    '76.53.110.207',
    '241.27.20.74',
    '252.9.109.47',
    '34.71.130.176',
    '51.177.159.194',
    '125.183.104.209',
    '214.29.56.253',
    '233.196.176.19',
    '34.71.130.177']
ipv6_raw = [
    '6ab3::ca1f:c840:f952:b286:25f2',
    '6ab3:aaaa::ca1f:c840:f952:b286:25f2',
    '::aaaa',
    'aaaa::',
    '536c:b906:3f24:5124:5e43:d9ee:22d8:6c30',
    '536f:ae86:fc5e:4cf9:f308:838a:8dc5:d758',
    '98b6:b97e:aa7d:96e:2333:c6f1:d83e:66eb',
    'bde7:8615:1359:4359:5171:d111:86f8:6361',
    'eac1:a1bc:1e0b:d8d2:60d0:b33b:1b95:7339',
    '5f5c:d1e:a89d:5f88:7dec:97fa:44e3:ff4c',
    '8525:ea6e:72b6:c4d7:848c:84d4:87e7:dca0',
    '317c:1552:1681:86ef:fa8:9aff:fbb1:c324',
    '317c:1552:1681:86ef:fa8:9aff:fbb0:0000',
    '97c4:26d2:b0ba:1003:ff99:ea1d:dcb0:9f63',
    'e28c:f4db:ad75:cb0d:c354:4ebf:d5dd:2d3f',
    'da6c:9958:f119:8bf7:f64e:8f89:bd2b:d52'
]


"""
Here unpacking ipv6 input data.
"""
unpack_ipv6(ipv6_raw)


"""
try/catch to catch invalid ipv4 or ipv6 format.
"""
try:
    """
    By key argument and lambdas in it we can sort 
    ip by octets.
    Lambda sequence in key argument just
    transforms ip octets to right form to sort.
    Example: 192.192.3.5 -> 192.192.003.005 (while sorting).
    Len mean count of octet digits.
    The same with ipv6.
    """
    ipv4 = sorted(ipv4_raw,
                  key=lambda x: int(''.join((
                                        lambda a:
                                            lambda v: a(a, v))(
                                                lambda s, x: x if len(x) == 3 else s(s, '0'+x))(i)
                                            for i in x.split('.'))))

    ipv6 = sorted(ipv6_raw,
                  key=lambda x: int(''.join((
                                        lambda a:
                                            lambda v: a(a, v))(
                                                lambda s, x: x if len(x) == 4 else s(s, '0'+x))(i)
                                                    for i in x.split(':')), 16))
except RecursionError:
    """
    Raising error with description
    """
    raise Exception('ipv4 or ipv6 contains too much bytes')


"""
Output for checking the result.
If you want you can remove these two
lines below.
"""
print(ipv4)
print(ipv6)
