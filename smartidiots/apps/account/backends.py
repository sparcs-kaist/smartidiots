from django.contrib.auth.models import User
import ldap

class AuthLDAPBackend:
    def authenticate(self, username=None, password=None):
        uri = 'ldap://143.248.234.102/'
        l = ldap.initialize(uri)
        dn = 'uid=%s,ou=People,dc=sparcs,dc=org' % username
        pw = password
        try:
            l.simple_bind_s(dn, pw)

            #l2 = ldap.initialize(uri)
            #result = l2.search_s(dn, ldap.SCOPE_SUBTREE, '(gidNumber=200)', ['cn'])

            #if len(result) == 1:
            #    valid = True
            #else:
            #    valid = False
            valid = True
        except (ldap.INVALID_CREDENTIALS, ldap.LDAPError):
            valid = False

        if valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username, password='not used')
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
