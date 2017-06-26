# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='paymentrequest.proto',
  package='payments',
  serialized_pb='\n\x14paymentrequest.proto\x12\x08payments\"+\n\x06Output\x12\x11\n\x06\x61mount\x18\x01 \x01(\x04:\x01\x30\x12\x0e\n\x06script\x18\x02 \x02(\x0c\"\xa3\x01\n\x0ePaymentDetails\x12\x15\n\x07network\x18\x01 \x01(\t:\x04main\x12!\n\x07outputs\x18\x02 \x03(\x0b\x32\x10.payments.Output\x12\x0c\n\x04time\x18\x03 \x02(\x04\x12\x0f\n\x07\x65xpires\x18\x04 \x01(\x04\x12\x0c\n\x04memo\x18\x05 \x01(\t\x12\x13\n\x0bpayment_url\x18\x06 \x01(\t\x12\x15\n\rmerchant_data\x18\x07 \x01(\x0c\"\x95\x01\n\x0ePaymentRequest\x12\"\n\x17payment_details_version\x18\x01 \x01(\r:\x01\x31\x12\x16\n\x08pki_type\x18\x02 \x01(\t:\x04none\x12\x10\n\x08pki_data\x18\x03 \x01(\x0c\x12\"\n\x1aserialized_payment_details\x18\x04 \x02(\x0c\x12\x11\n\tsignature\x18\x05 \x01(\x0c\"\'\n\x10X509Certificates\x12\x13\n\x0b\x63\x65rtificate\x18\x01 \x03(\x0c\"i\n\x07Payment\x12\x15\n\rmerchant_data\x18\x01 \x01(\x0c\x12\x14\n\x0ctransactions\x18\x02 \x03(\x0c\x12#\n\trefund_to\x18\x03 \x03(\x0b\x32\x10.payments.Output\x12\x0c\n\x04memo\x18\x04 \x01(\t\">\n\nPaymentACK\x12\"\n\x07payment\x18\x01 \x02(\x0b\x32\x11.payments.Payment\x12\x0c\n\x04memo\x18\x02 \x01(\tB(\n\x1eorg.bitcoin.protocols.paymentsB\x06Protos')




_OUTPUT = descriptor.Descriptor(
  name='Output',
  full_name='payments.Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='amount', full_name='payments.Output.amount', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='script', full_name='payments.Output.script', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=34,
  serialized_end=77,
)


_PAYMENTDETAILS = descriptor.Descriptor(
  name='PaymentDetails',
  full_name='payments.PaymentDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='network', full_name='payments.PaymentDetails.network', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("main", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='outputs', full_name='payments.PaymentDetails.outputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time', full_name='payments.PaymentDetails.time', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='expires', full_name='payments.PaymentDetails.expires', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='memo', full_name='payments.PaymentDetails.memo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='payment_url', full_name='payments.PaymentDetails.payment_url', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='merchant_data', full_name='payments.PaymentDetails.merchant_data', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=80,
  serialized_end=243,
)


_PAYMENTREQUEST = descriptor.Descriptor(
  name='PaymentRequest',
  full_name='payments.PaymentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='payment_details_version', full_name='payments.PaymentRequest.payment_details_version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pki_type', full_name='payments.PaymentRequest.pki_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("none", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pki_data', full_name='payments.PaymentRequest.pki_data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='serialized_payment_details', full_name='payments.PaymentRequest.serialized_payment_details', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='signature', full_name='payments.PaymentRequest.signature', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=246,
  serialized_end=395,
)


_X509CERTIFICATES = descriptor.Descriptor(
  name='X509Certificates',
  full_name='payments.X509Certificates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='certificate', full_name='payments.X509Certificates.certificate', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=397,
  serialized_end=436,
)


_PAYMENT = descriptor.Descriptor(
  name='Payment',
  full_name='payments.Payment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='merchant_data', full_name='payments.Payment.merchant_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='transactions', full_name='payments.Payment.transactions', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='refund_to', full_name='payments.Payment.refund_to', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='memo', full_name='payments.Payment.memo', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=438,
  serialized_end=543,
)


_PAYMENTACK = descriptor.Descriptor(
  name='PaymentACK',
  full_name='payments.PaymentACK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='payment', full_name='payments.PaymentACK.payment', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='memo', full_name='payments.PaymentACK.memo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=545,
  serialized_end=607,
)

_PAYMENTDETAILS.fields_by_name['outputs'].message_type = _OUTPUT
_PAYMENT.fields_by_name['refund_to'].message_type = _OUTPUT
_PAYMENTACK.fields_by_name['payment'].message_type = _PAYMENT
DESCRIPTOR.message_types_by_name['Output'] = _OUTPUT
DESCRIPTOR.message_types_by_name['PaymentDetails'] = _PAYMENTDETAILS
DESCRIPTOR.message_types_by_name['PaymentRequest'] = _PAYMENTREQUEST
DESCRIPTOR.message_types_by_name['X509Certificates'] = _X509CERTIFICATES
DESCRIPTOR.message_types_by_name['Payment'] = _PAYMENT
DESCRIPTOR.message_types_by_name['PaymentACK'] = _PAYMENTACK

class Output(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OUTPUT

  # @@protoc_insertion_point(class_scope:payments.Output)

class PaymentDetails(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PAYMENTDETAILS

  # @@protoc_insertion_point(class_scope:payments.PaymentDetails)

class PaymentRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PAYMENTREQUEST

  # @@protoc_insertion_point(class_scope:payments.PaymentRequest)

class X509Certificates(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _X509CERTIFICATES

  # @@protoc_insertion_point(class_scope:payments.X509Certificates)

class Payment(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PAYMENT

  # @@protoc_insertion_point(class_scope:payments.Payment)

class PaymentACK(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PAYMENTACK

  # @@protoc_insertion_point(class_scope:payments.PaymentACK)

# @@protoc_insertion_point(module_scope)
