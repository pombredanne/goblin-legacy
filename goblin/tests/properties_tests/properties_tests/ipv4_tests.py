from __future__ import unicode_literals

import ipaddress
from nose.plugins.attrib import attr

from tornado.testing import gen_test
from .base_tests import GraphPropertyBaseClassTestCase, create_key
from goblin.properties.properties import IPV4
from goblin.models import Vertex
from goblin._compat import print_


# @attr('unit', 'property', 'property_ipv4')
# class IPV4PropertyTestCase(GraphPropertyBaseClassTestCase):
#     klass = IPV4
#     good_cases = (ipaddress.IPv4Address('1.2.3.4'), '1.2.3.4', '0.0.0.0',
#                   '255.255.255.255')
#     bad_cases = ('0', '0.', '0.0', '0.0.', '0.0.0', '0.0.0.',
#                  '256.256.256.256', '1.2.3.256',
#                  ipaddress.IPv6Address('1:2:3:4:5:6:7:8'))
#
#     def test_ipv4_default_cases(self):
#         p = IPV4(default='1.2.3.4')

class IPV4TestVertex(Vertex):
    element_type = 'test_ipv4_vertex'

    test_val = IPV4()


@attr('unit', 'property', 'property_ipv4')
class IPV4VertexTestCase(GraphPropertyBaseClassTestCase):

    @gen_test
    def test_ipv4_io(self):
        print_("creating vertex")
        key = IPV4TestVertex.get_property_by_name('test_val')
        yield create_key(key, 'String')
        dt = yield IPV4TestVertex.create(
            test_val=ipaddress.IPv4Address('1.2.3.4'))
        print_("getting vertex from vertex: %s" % dt)
        dt2 = yield IPV4TestVertex.get(dt._id)
        print_("got vertex: %s\n" % dt2)
        self.assertEqual(dt2.test_val, dt.test_val)
        print_("deleting vertex")
        yield dt2.delete()

        dt3 = yield IPV4TestVertex.create(test_val='4.3.2.1')
        print_("\ncreated vertex: %s" % dt)
        dt4 = yield IPV4TestVertex.get(dt3._id)
        print_("Got vertex: %s" % dt4)
        self.assertIsInstance(dt4.test_val, ipaddress.IPv4Address)
        self.assertEqual(str(dt4.test_val), '4.3.2.1')
        print_("deleting vertex")
        yield dt3.delete()
