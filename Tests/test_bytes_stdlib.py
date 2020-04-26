# Licensed to the .NET Foundation under one or more agreements.
# The .NET Foundation licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information.

##
## Run selected tests from test_bytes from StdLib
##

import unittest
import sys

from iptest import run_test

import test.test_bytes

def load_tests(loader, standard_tests, pattern):
    if sys.implementation.name == 'ironpython':
        suite = unittest.TestSuite()
        suite.addTest(test.test_bytes.AssortedBytesTest('test_compare'))
        suite.addTest(test.test_bytes.AssortedBytesTest('test_compare_bytes_to_bytearray'))
        suite.addTest(test.test_bytes.AssortedBytesTest('test_doc'))
        suite.addTest(test.test_bytes.AssortedBytesTest('test_from_bytearray'))
        suite.addTest(test.test_bytes.AssortedBytesTest('test_literal'))
        suite.addTest(test.test_bytes.AssortedBytesTest('test_repr_str'))
        suite.addTest(test.test_bytes.AssortedBytesTest('test_return_self'))
        suite.addTest(test.test_bytes.AssortedBytesTest('test_rsplit_bytearray'))
        suite.addTest(test.test_bytes.AssortedBytesTest('test_split_bytearray'))
        suite.addTest(test.test_bytes.AssortedBytesTest('test_to_str'))
        suite.addTest(test.test_bytes.AssortedBytesTest('test_translate'))
        suite.addTest(test.test_bytes.ByteArrayAsStringTest('test_contains'))
        suite.addTest(test.test_bytes.ByteArrayAsStringTest('test_count'))
        suite.addTest(test.test_bytes.ByteArrayAsStringTest('test_expandtabs'))
        suite.addTest(test.test_bytes.ByteArrayAsStringTest('test_find'))
        suite.addTest(test.test_bytes.ByteArrayAsStringTest('test_index'))
        suite.addTest(test.test_bytes.ByteArrayAsStringTest('test_lower'))
        suite.addTest(test.test_bytes.ByteArrayAsStringTest('test_replace'))
        suite.addTest(test.test_bytes.ByteArrayAsStringTest('test_replace_overflow'))
        suite.addTest(test.test_bytes.ByteArrayAsStringTest('test_rfind'))
        suite.addTest(test.test_bytes.ByteArrayAsStringTest('test_rindex'))
        suite.addTest(test.test_bytes.ByteArrayAsStringTest('test_rsplit'))
        suite.addTest(test.test_bytes.ByteArrayAsStringTest('test_split'))
        suite.addTest(test.test_bytes.ByteArrayAsStringTest('test_upper'))
        suite.addTest(test.test_bytes.ByteArraySubclassTest('test_basic'))
        suite.addTest(test.test_bytes.ByteArraySubclassTest('test_copy'))
        suite.addTest(test.test_bytes.ByteArraySubclassTest('test_init_override'))
        suite.addTest(test.test_bytes.ByteArraySubclassTest('test_join'))
        suite.addTest(test.test_bytes.ByteArraySubclassTest('test_pickle'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_alloc'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_append'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_basics'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_bytearray_api'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_center'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_clear'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_compare'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_compare_to_str'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_concat'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_constructor_overflow'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_constructor_type_errors'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_constructor_value_errors'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_contains'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_copied'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_copy'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_count'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_decode'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_del_expand'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_delitem'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_empty_sequence'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_encoding'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_endswith'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_extend'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_extended_getslice'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_extended_set_del_slice'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_fifo_overrun'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_find'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_find_etc_raise_correct_error_messages'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_from_index'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_from_int'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_from_list'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_from_ssize'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_fromhex'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_getslice'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_iconcat'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_index'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_init_alloc'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_insert'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_integer_arguments_out_of_byte_range'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_irepeat'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_irepeat_1char'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_iterator_pickling'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_join'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_ljust'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_lstrip'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_maketrans'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_nohash'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_none_arguments'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_nosort'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_ord'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_partition'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_partition_bytearray_doesnt_share_nullstring'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_pickling'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_pop'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_regexps'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_remove'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_repeat'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_repeat_1char'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_replace'))
        #suite.addTest(test.test_bytes.ByteArrayTest('test_resize_forbidden'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_reverse'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_reversed'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_rfind'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_rindex'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_rjust'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_rpartition'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_rsplit'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_rsplit_string_error'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_rsplit_unicodewhitespace'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_rsplit_whitespace'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_rstrip'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_setitem'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_setslice'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_setslice_extend'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_setslice_trap'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_split'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_split_string_error'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_split_unicodewhitespace'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_split_whitespace'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_startswith'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_strip'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_strip_bytearray'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_strip_string_error'))
        suite.addTest(test.test_bytes.ByteArrayTest('test_strip_whitespace'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_capitalize'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_center'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_expandtabs'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_isalnum'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_isalpha'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_isdigit'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_islower'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_isspace'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_istitle'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_isupper'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_ljust'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_lower'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_returns_new_copy'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_rjust'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_splitlines'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_swapcase'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_title'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_upper'))
        suite.addTest(test.test_bytes.BytearrayPEP3137Test('test_zfill'))
        suite.addTest(test.test_bytes.BytesAsStringTest('test_contains'))
        suite.addTest(test.test_bytes.BytesAsStringTest('test_count'))
        suite.addTest(test.test_bytes.BytesAsStringTest('test_expandtabs'))
        suite.addTest(test.test_bytes.BytesAsStringTest('test_find'))
        suite.addTest(test.test_bytes.BytesAsStringTest('test_index'))
        suite.addTest(test.test_bytes.BytesAsStringTest('test_lower'))
        suite.addTest(test.test_bytes.BytesAsStringTest('test_replace'))
        suite.addTest(test.test_bytes.BytesAsStringTest('test_replace_overflow'))
        suite.addTest(test.test_bytes.BytesAsStringTest('test_rfind'))
        suite.addTest(test.test_bytes.BytesAsStringTest('test_rindex'))
        suite.addTest(test.test_bytes.BytesAsStringTest('test_rsplit'))
        suite.addTest(test.test_bytes.BytesAsStringTest('test_split'))
        suite.addTest(test.test_bytes.BytesAsStringTest('test_upper'))
        suite.addTest(test.test_bytes.BytesSubclassTest('test_basic'))
        suite.addTest(test.test_bytes.BytesSubclassTest('test_copy'))
        suite.addTest(test.test_bytes.BytesSubclassTest('test_join'))
        suite.addTest(test.test_bytes.BytesSubclassTest('test_pickle'))
        suite.addTest(test.test_bytes.BytesTest('test_basics'))
        suite.addTest(test.test_bytes.BytesTest('test_buffer_is_readonly'))
        suite.addTest(test.test_bytes.BytesTest('test_center'))
        suite.addTest(test.test_bytes.BytesTest('test_compare'))
        suite.addTest(test.test_bytes.BytesTest('test_compare_to_str'))
        suite.addTest(test.test_bytes.BytesTest('test_concat'))
        suite.addTest(test.test_bytes.BytesTest('test_constructor_overflow'))
        suite.addTest(test.test_bytes.BytesTest('test_constructor_type_errors'))
        suite.addTest(test.test_bytes.BytesTest('test_constructor_value_errors'))
        suite.addTest(test.test_bytes.BytesTest('test_contains'))
        suite.addTest(test.test_bytes.BytesTest('test_copy'))
        suite.addTest(test.test_bytes.BytesTest('test_count'))
        #suite.addTest(test.test_bytes.BytesTest('test_custom'))
        suite.addTest(test.test_bytes.BytesTest('test_decode'))
        suite.addTest(test.test_bytes.BytesTest('test_empty_sequence'))
        suite.addTest(test.test_bytes.BytesTest('test_encoding'))
        suite.addTest(test.test_bytes.BytesTest('test_endswith'))
        suite.addTest(test.test_bytes.BytesTest('test_extended_getslice'))
        suite.addTest(test.test_bytes.BytesTest('test_find'))
        suite.addTest(test.test_bytes.BytesTest('test_find_etc_raise_correct_error_messages'))
        #suite.addTest(test.test_bytes.BytesTest('test_from_format'))
        suite.addTest(test.test_bytes.BytesTest('test_from_index'))
        suite.addTest(test.test_bytes.BytesTest('test_from_int'))
        suite.addTest(test.test_bytes.BytesTest('test_from_list'))
        suite.addTest(test.test_bytes.BytesTest('test_from_ssize'))
        suite.addTest(test.test_bytes.BytesTest('test_fromhex'))
        suite.addTest(test.test_bytes.BytesTest('test_getslice'))
        suite.addTest(test.test_bytes.BytesTest('test_index'))
        suite.addTest(test.test_bytes.BytesTest('test_integer_arguments_out_of_byte_range'))
        suite.addTest(test.test_bytes.BytesTest('test_iterator_pickling'))
        suite.addTest(test.test_bytes.BytesTest('test_join'))
        suite.addTest(test.test_bytes.BytesTest('test_ljust'))
        suite.addTest(test.test_bytes.BytesTest('test_lstrip'))
        suite.addTest(test.test_bytes.BytesTest('test_maketrans'))
        suite.addTest(test.test_bytes.BytesTest('test_none_arguments'))
        suite.addTest(test.test_bytes.BytesTest('test_ord'))
        suite.addTest(test.test_bytes.BytesTest('test_partition'))
        suite.addTest(test.test_bytes.BytesTest('test_pickling'))
        suite.addTest(test.test_bytes.BytesTest('test_repeat'))
        suite.addTest(test.test_bytes.BytesTest('test_repeat_1char'))
        suite.addTest(test.test_bytes.BytesTest('test_replace'))
        suite.addTest(test.test_bytes.BytesTest('test_reversed'))
        suite.addTest(test.test_bytes.BytesTest('test_rfind'))
        suite.addTest(test.test_bytes.BytesTest('test_rindex'))
        suite.addTest(test.test_bytes.BytesTest('test_rjust'))
        suite.addTest(test.test_bytes.BytesTest('test_rpartition'))
        suite.addTest(test.test_bytes.BytesTest('test_rsplit'))
        suite.addTest(test.test_bytes.BytesTest('test_rsplit_string_error'))
        suite.addTest(test.test_bytes.BytesTest('test_rsplit_unicodewhitespace'))
        suite.addTest(test.test_bytes.BytesTest('test_rsplit_whitespace'))
        suite.addTest(test.test_bytes.BytesTest('test_rstrip'))
        suite.addTest(test.test_bytes.BytesTest('test_split'))
        suite.addTest(test.test_bytes.BytesTest('test_split_string_error'))
        suite.addTest(test.test_bytes.BytesTest('test_split_unicodewhitespace'))
        suite.addTest(test.test_bytes.BytesTest('test_split_whitespace'))
        suite.addTest(test.test_bytes.BytesTest('test_startswith'))
        suite.addTest(test.test_bytes.BytesTest('test_strip'))
        suite.addTest(test.test_bytes.BytesTest('test_strip_bytearray'))
        suite.addTest(test.test_bytes.BytesTest('test_strip_string_error'))
        suite.addTest(test.test_bytes.BytesTest('test_strip_whitespace'))
        return suite

    else:
        return loader.loadTestsFromModule(test.test_bytes, pattern)

run_test(__name__)
