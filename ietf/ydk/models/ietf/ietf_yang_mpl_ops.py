""" ietf_yang_mpl_ops 

This module contains information about the operation of
the MPL protocol.

Copyright (c) 2016 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or

without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC XXXX; see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class MplOps(object):
    """
    Parameter settings for each MPL server and for each
    individual domain of the server.
    
    .. attribute:: mpl_parameter
    
    	Each domain has a set of MPL forwarding parameters
    	**type**\: list of    :py:class:`MplParameter <ydk.models.ietf.ietf_yang_mpl_ops.MplOps.MplParameter>`
    
    .. attribute:: proactive_forwarding
    
    	The boolean value indicates whether the MPL forwarder
    	**type**\:  bool
    
    .. attribute:: se_lifetime
    
    	lifetime in milliseconds/(mpl timer units),
    	**type**\:  int
    
    	**range:** 0..65535
    
    .. attribute:: seed_set_entry_lifetime
    
    	The value indicates the minimum lifetime for an entry
    	**type**\:  int
    
    	**range:** 0..18446744073709551615
    
    

    """

    _prefix = 'mpl'
    _revision = '2016-10-25'

    def __init__(self):
        self.mpl_parameter = YList()
        self.mpl_parameter.parent = self
        self.mpl_parameter.name = 'mpl_parameter'
        self.proactive_forwarding = None
        self.se_lifetime = None
        self.seed_set_entry_lifetime = None


    class MplParameter(object):
        """
        Each domain has a set of MPL forwarding parameters
        which regulate the forwarding operation.
        
        .. attribute:: domainid  <key>
        
        	Each domainID must be present in
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: control_message_imax
        
        	The maximum Trickle timer interval, as defined
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: control_message_imin
        
        	The minimum Trickle timer interval, as defined
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: control_message_k
        
        	The redundancy constant, as defined in [RFC6206],
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**default value**\: 1
        
        .. attribute:: control_message_timer_expirations
        
        	The number of Trickle time expirations that occur
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**default value**\: 10
        
        .. attribute:: data_message_imax
        
        	The maximum Trickle timer interval, as defined in
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: data_message_imin
        
        	The minimum Trickle timer interval, as defined in
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: data_message_k
        
        	The redundancy constant, as defined in [RFC6206], for
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**default value**\: 1
        
        .. attribute:: data_message_timer_expirations
        
        	The number of Trickle timer expirations that occur
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**default value**\: 3
        
        

        """

        _prefix = 'mpl'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.domainid = None
            self.control_message_imax = None
            self.control_message_imin = None
            self.control_message_k = None
            self.control_message_timer_expirations = None
            self.data_message_imax = None
            self.data_message_imin = None
            self.data_message_k = None
            self.data_message_timer_expirations = None

        @property
        def _common_path(self):
            if self.domainid is None:
                raise YPYModelError('Key property domainid is None')

            return '/ietf-yang-mpl-ops:mpl-ops/ietf-yang-mpl-ops:mpl-parameter[ietf-yang-mpl-ops:domainID = ' + str(self.domainid) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.domainid is not None:
                return True

            if self.control_message_imax is not None:
                return True

            if self.control_message_imin is not None:
                return True

            if self.control_message_k is not None:
                return True

            if self.control_message_timer_expirations is not None:
                return True

            if self.data_message_imax is not None:
                return True

            if self.data_message_imin is not None:
                return True

            if self.data_message_k is not None:
                return True

            if self.data_message_timer_expirations is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_yang_mpl_ops as meta
            return meta._meta_table['MplOps.MplParameter']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-yang-mpl-ops:mpl-ops'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.mpl_parameter is not None:
            for child_ref in self.mpl_parameter:
                if child_ref._has_data():
                    return True

        if self.proactive_forwarding is not None:
            return True

        if self.se_lifetime is not None:
            return True

        if self.seed_set_entry_lifetime is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_yang_mpl_ops as meta
        return meta._meta_table['MplOps']['meta_info']

