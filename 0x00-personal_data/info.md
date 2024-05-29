task 0
How does the job work?
    the loop itreates over each field name in the fields list
    => fields = ["password", "date_of_birth"]
    why ? -- To process and obfuscate each specified field one by one.

message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator,
                         message)

lets breakdown >>
    field + "=.*?" + separator
     => matches the fieldName followed by an "=" and matches any character up to the next occurrence of the seprator ";"
    field + "=" + redaction + separator
     => matches the fieldName and "=" as `email=` and replace the original field value with the redaction  string "xxx" followed by the seprator.

    why ? To obfuscate the value of the specified field in the message.
=====================================
task 1