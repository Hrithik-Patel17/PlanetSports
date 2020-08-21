$(document).ready(function() {
  /********* User Sign in **************/

  $("#user_login_button").click(function(e) {
    console.log("button clicked");
    //e.preventDefault();
    $("#user_login").validate({
      rules: {
        email: {
          required: true
          //email : true,
        },
        password: {
          required: true
        }
      },
      messages: {
        email: {
          required: "This field is mandatory"
          //email : "Not valid Email",
        },
        password: {
          required: "This field is mandatory"
        }
      },
      errorPlacement: function(error, element) {
        var name = $(element).attr("name");
        error.appendTo($("#" + name + "_validate"));
      }
    });

    //$('#health_checkup_plans').submit();
  });

  $.validator.addMethod("checkname", function(value, element) {
    if (!value.trim()) return false;
    else return true;
  });
  $.validator.addMethod("validName", function(value, element) {
    return this.optional(element) || value == value.match(/^[a-zA-Z\s]+$/);
    // --                                    or leave a space here ^^
  });
  jQuery.validator.addMethod("validMobile", function(phone_number, element) {
    return this.optional(element) || phone_number.match(/^[0-9]/);
  });

  /********* User Sign in **************/

  /********* User Register **************/

  $("#user_register_button").click(function(e) {
    //console.log('button clicked');
    //e.preventDefault();
    $("#user_register").validate({
      rules: {
        firstname: {
          required: true,
          checkname: true,
          validName: true,
          minlength: 3
        },
        email: {
          required: true,
          email: true
        },
        telephone: {
          required: true,
          validMobile: true,
          minlength: 10,
          maxlength: 10
        },
        city: {
          required: true
        },
        agree: {
          required: true
        }
      },
      messages: {
        firstname: {
          required: "This field is mandatory",
          checkname: "Please enter letters only",
          validName: "Please enter letters only",
          minlength: "Name must be at least 3 character"
        },
        email: {
          required: "This field is mandatory",
          email: "Not valid Email"
        },
        telephone: {
          required: "This field is mandatory",
          validMobile: "Please enter digits only",
          minlength: "Mobile No. must be 10 digits",
          maxlength: "Mobile No. must be 10 digits"
        },
        city: {
          required: "This field is mandatory"
        },
        agree: {
          required: "This field is mandatory"
        }
      },
      errorPlacement: function(error, element) {
        var name = $(element).attr("name");
        error.appendTo($("#" + name + "_validate"));
      }
    });

    //$('#health_checkup_plans').submit();
  });

  $.validator.addMethod("checkname", function(value, element) {
    if (!value.trim()) return false;
    else return true;
  });
  $.validator.addMethod("validName", function(value, element) {
    return this.optional(element) || value == value.match(/^[a-zA-Z\s]+$/);
    // --                                    or leave a space here ^^
  });
  jQuery.validator.addMethod("validMobile", function(phone_number, element) {
    return this.optional(element) || phone_number.match(/^[0-9]/);
  });

  /********* User Register **************/

  /********* Forgot Password ************/

  $("#forgot_pass_button").click(function(e) {
    console.log("button clicked");
    //e.preventDefault();
    $("#forgot_pass").validate({
      rules: {
        email: {
          required: true,
          email: true
        }
      },
      messages: {
        email: {
          required: "This field is mandatory",
          email: "Not valid Email"
        }
      },
      errorPlacement: function(error, element) {
        var name = $(element).attr("name");
        error.appendTo($("#" + name + "_validate"));
      }
    });

    //$('#health_checkup_plans').submit();
  });

  $.validator.addMethod("checkname", function(value, element) {
    if (!value.trim()) return false;
    else return true;
  });
  $.validator.addMethod("validName", function(value, element) {
    return this.optional(element) || value == value.match(/^[a-zA-Z\s]+$/);
    // --                                    or leave a space here ^^
  });
  jQuery.validator.addMethod("validMobile", function(phone_number, element) {
    return this.optional(element) || phone_number.match(/^[0-9]/);
  });

  /********* Forgot Password ************/

  /********* Company Sign in **************/

  $("#company_login_button").click(function(e) {
    console.log("button clicked");
    //e.preventDefault();
    $("#company_login").validate({
      rules: {
        email: {
          required: true,
          email: true
        },
        password: {
          required: true
        }
      },
      messages: {
        email: {
          required: "This field is mandatory",
          email: "Not valid Email"
        },
        password: {
          required: "This field is mandatory"
        }
      },
      errorPlacement: function(error, element) {
        var name = $(element).attr("name");
        error.appendTo($("#" + name + "_validate"));
      }
    });

    //$('#health_checkup_plans').submit();
  });

  $.validator.addMethod("checkname", function(value, element) {
    if (!value.trim()) return false;
    else return true;
  });
  $.validator.addMethod("validName", function(value, element) {
    return this.optional(element) || value == value.match(/^[a-zA-Z\s]+$/);
    // --                                    or leave a space here ^^
  });
  jQuery.validator.addMethod("validMobile", function(phone_number, element) {
    return this.optional(element) || phone_number.match(/^[0-9]/);
  });

  /********* Company Sign in **************/

  /********* Company Register **************/

  $("#company_register_button").click(function(e) {
    console.log("button clicked");
    //e.preventDefault();
    $("#company_register").validate({
      rules: {
        shoppartner: {
          required: true,
          checkname: true,
          validName: true,
          minlength: 3
        },
        address_1: {
          required: true
        },
        entity: {
          required: true
        },
        company_cin: {
          required: {
            depends: function() {
              return $("#input-entity").val() == "Private Limited"
                ? true
                : $("#input-entity").val() == "Public Limited"
                ? true
                : $("#input-entity").val() == "LLP"
                ? true
                : false;
              // return ($("#input-entity").val() == "Public Limited");
              // return ($("#input-entity").val() == "LLP");
            }
          }
        },
        // yes : {
        // required : true,
        // },
        // company_service_tax: {
        // required: {
        // depends: function() {
        // return ($("#input-yesCheck:checked").val() == 'yes');
        // }
        // }
        // },

        country_id: {
          required: true
        },
        company_pan: {
          required: true
        },
        zone_id: {
          required: true
        },

        owner_email: {
          required: true,
          email: true
        },
        telephone: {
          required: true,
          validMobile: true,
          minlength: 10,
          maxlength: 10
        },
        city: {
          required: true
        },
        firstname: {
          required: true,
          checkname: true,
          validName: true,
          minlength: 3
        },
        email: {
          required: true,
          email: true
        },
        owner_telephone: {
          required: true,
          validMobile: true,
          minlength: 10,
          maxlength: 10
        },
        agree: {
          required: true
        }
      },
      messages: {
        shoppartner: {
          required: "This field is mandatory",
          checkname: "Please enter letters only",
          validName: "Please enter letters only",
          minlength: "Name must be at least 3 character"
        },
        address_1: {
          required: "This field is mandatory"
        },
        entity: {
          required: "This field is mandatory"
        },
        yes: {
          required: "This field is mandatory"
        },
        company_service_tax: {
          required: "This field is mandatory"
        },
        country_id: {
          required: "This field is mandatory"
        },
        company_pan: {
          required: "This field is mandatory"
        },

        zone_id: {
          required: "This field is mandatory"
        },
        owner_email: {
          required: "This field is mandatory",
          email: "Not valid Email"
        },
        telephone: {
          required: "This field is mandatory",
          validMobile: "Please enter digits only",
          minlength: "Mobile No. must be 10 digits",
          maxlength: "Mobile No. must be 10 digits"
        },
        city: {
          required: "This field is mandatory"
        },
        firstname: {
          required: "This field is mandatory",
          checkname: "Please enter letters only",
          validName: "Please enter letters only",
          minlength: "Name must be at least 3 character"
        },
        email: {
          required: "This field is mandatory",
          email: "Not valid Email"
        },
        owner_telephone: {
          required: "This field is mandatory",
          validMobile: "Please enter digits only",
          minlength: "Mobile No. must be 10 digits",
          maxlength: "Mobile No. must be 10 digits"
        },

        agree: {
          required: "This field is mandatory"
        }
      },
      errorPlacement: function(error, element) {
        var name = $(element).attr("name");
        error.appendTo($("#" + name + "_validate"));
      }
    });

    //$('#health_checkup_plans').submit();
  });

  $.validator.addMethod("checkname", function(value, element) {
    if (!value.trim()) return false;
    else return true;
  });
  $.validator.addMethod("validName", function(value, element) {
    return this.optional(element) || value == value.match(/^[a-zA-Z\s]+$/);
    // --                                    or leave a space here ^^
  });
  jQuery.validator.addMethod("validMobile", function(phone_number, element) {
    return this.optional(element) || phone_number.match(/^[0-9]/);
  });

  /********* Company Register **************/

  /*************** Edit Venue Profile ************************/

  $("#edit_venue_profile_button").click(function(e) {
    //console.log('button clicked');
    //e.preventDefault();
    $("#edit_venue_profile").validate({
      rules: {
        firstname: {
          required: true,
          checkname: true,
          validName: true,
          minlength: 3
        },
        email: {
          required: true,
          email: true
        },
        telephone: {
          required: true,
          validMobile: true,
          minlength: 10,
          maxlength: 10
        },
        city: {
          required: true
        },

        fax: {
          required: true
        },
        dob: {
          required: true
        }
      },
      messages: {
        firstname: {
          required: "This field is mandatory",
          checkname: "Please enter letters only",
          validName: "Please enter letters only",
          minlength: "Name must be at least 3 character"
        },
        email: {
          required: "This field is mandatory",
          email: "Not valid Email"
        },
        telephone: {
          required: "This field is mandatory",
          validMobile: "Please enter digits only",
          minlength: "Mobile No. must be 10 digits",
          maxlength: "Mobile No. must be 10 digits"
        },
        city: {
          required: "This field is mandatory"
        },
        fax: {
          required: "This field is mandatory"
        },
        dob: {
          required: "This field is mandatory"
        }
      },
      errorPlacement: function(error, element) {
        var name = $(element).attr("name");
        error.appendTo($("#" + name + "_validate"));
      }
    });

    //$('#health_checkup_plans').submit();
  });

  $.validator.addMethod("checkname", function(value, element) {
    if (!value.trim()) return false;
    else return true;
  });
  $.validator.addMethod("validName", function(value, element) {
    return this.optional(element) || value == value.match(/^[a-zA-Z\s]+$/);
    // --                                    or leave a space here ^^
  });
  jQuery.validator.addMethod("validMobile", function(phone_number, element) {
    return this.optional(element) || phone_number.match(/^[0-9]/);
  });

  /********* Forgot Password ************/

  $("#change_venue_password_button").click(function(e) {
    console.log("button clicked");
    //e.preventDefault();
    $("#change_venue_password").validate({
      rules: {
        password: {
          required: true
        },
        confirm: {
          required: true,
          equalTo: "#input-password"
        }
      },
      messages: {
        password: {
          required: "This field is mandatory"
        },
        confirm: {
          required: "This field is mandatory",
          equalTo: "Password does not match"
        }
      },
      errorPlacement: function(error, element) {
        var name = $(element).attr("name");
        error.appendTo($("#" + name + "_validate"));
      }
    });

    //$('#health_checkup_plans').submit();
  });

  $.validator.addMethod("checkname", function(value, element) {
    if (!value.trim()) return false;
    else return true;
  });
  $.validator.addMethod("validName", function(value, element) {
    return this.optional(element) || value == value.match(/^[a-zA-Z\s]+$/);
    // --                                    or leave a space here ^^
  });
  jQuery.validator.addMethod("validMobile", function(phone_number, element) {
    return this.optional(element) || phone_number.match(/^[0-9]/);
  });

  /********* Forgot Password ************/
});
