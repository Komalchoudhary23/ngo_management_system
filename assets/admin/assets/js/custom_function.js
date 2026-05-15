$("#change_photo").click(function () {
    $('#photo').show();
    $('#change_photo').remove();
}); 

$("#change_photo1").click(function () {
    $('#photo1').show();
    $('#change_photo1').remove();
}); 

$("#change_photo2").click(function () {
    $('#photo2').show();
    $('#change_photo2').remove();
}); 

$("#change_photo3").click(function () {
    $('#photo3').show();
    $('#change_photo3').remove();
}); 

$("#change_photo4").click(function () {
    $('#photo4').show();
    $('#change_photo4').remove();
});

$("#change_photo5").click(function () {
    $('#photo5').show();
    $('#change_photo5').remove();
});

$("#change_photo6").click(function () {
    $('#photo6').show();
    $('#change_photo6').remove();
});
$("#change_photo68").click(function () {
    $('#photo68').show();
    $('#change_photo68').remove();
});
$("#change_photo69").click(function () {
    $('#photo69').show();
    $('#change_photo69').remove();
});


function delete_banner(banner_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'banner/delete_banner';
    swal({
        title: "Are You Sure Delete Banner ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        banner_id: banner_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Deleted Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "Banner not Deleted",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}

function delete_events(events_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'events/delete_events';
    swal({
        title: "Are You Sure Delete Events ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        events_id: events_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Deleted Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "Events not Deleted",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}

function delete_donation(donation_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'donation/delete_donation';
    swal({
        title: "Are You Sure Delete Donation ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        donation_id: donation_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Deleted Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "Course not Deleted",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}

  
function delete_volunteer(volunteer_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'volunteer/delete_volunteer';
    swal({
        title: "Are You Sure Delete Volunteer ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        team_id: team_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Deleted Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "Team not Deleted",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}

 
function delete_user_testimonials(user_testimonial_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'testimonials/delete_user_testimonials';
    swal({
        title: "Are You Sure Delete User Testimonial ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        user_testimonial_id: user_testimonial_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Deleted Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "User Testimonial not Deleted",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}


function delete_donation_enquiry(donation_enquiry_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'enquiry/delete_donation_enquiry';
    swal({
        title: "Are You Sure Delete Donation Enquiry ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        donation_enquiry_id: donation_enquiry_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Deleted Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "Donation Enquiry Not Deleted",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}

function delete_contact_enquiry(contact_enquiry_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'enquiry/delete_contact_enquiry';
    swal({
        title: "Are You Sure Delete Contact Enquiry ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        contact_enquiry_id: contact_enquiry_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Deleted Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "Contact Enquiry Not Deleted",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}
 
function delete_blog(blog_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'blog/delete_blog';
    swal({
        title: "Are You Sure Delete Blog ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        blog_id: blog_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Deleted Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "Blog not Deleted",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}

 
function delete_staff(staff_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'staff/delete_staff';
    swal({
        title: "Are You Sure Delete Staff ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        staff_id: staff_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Deleted Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "Staff not Deleted",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}

function update_staff_status(staff_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'staff/update_staff_status';
    swal({
        title: "Are You Sure Update Staff Status ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        staff_id: staff_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Updated Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "Staff Status Not Updated",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}


function delete_user(user_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'user/delete_user';
    swal({
        title: "Are You Sure Delete User ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        user_id: user_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Deleted Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "User not Deleted",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}

function update_user_status(user_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'user/update_user_status';
    swal({
        title: "Are You Sure Update User Status ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        user_id: user_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Updated Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "User Status Not Updated",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}
 

function delete_role(role_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'role/delete_role';
    swal({
        title: "Are You Sure Delete Role ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        role_id: role_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Deleted Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "User not Deleted",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}

function update_role_status(role_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'role/update_role_status';
    swal({
        title: "Are You Sure Update Role Status ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        role_id: role_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Updated Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "Role Status Not Updated",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}
  

function delete_testimonial(testimonial_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'testimonial/delete_testimonial';
    swal({
        title: "Are You Sure Delete Testimonial ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        testimonial_id: testimonial_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Deleted Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "Testimonial not Deleted",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}

function update_testimonial_status(testimonial_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'testimonial/update_testimonial_status';
    swal({
        title: "Are You Sure Update Testimonial Status ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        testimonial_id: testimonial_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Updated Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "Testimonial Status Not Updated",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}
  

function delete_course_enquiry(course_id) {
    var base_url = $('#base_url').val();
    var url = base_url + 'enquiry/delete_course_enquiry';
    swal({
        title: "Are You Sure Delete Course Enquiry ?",
        //text: "You will not be able to recover this imaginary file!",
        type: "success",
        showCancelButton: true,
        confirmButtonColor: "#66BB6A",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        closeOnConfirm: false,
        closeOnCancel: false
    },
            function (isConfirm) {
                if (isConfirm) {
                    $.post(url, {
                        course_id: course_id
                    }, function (data) {
                        if (data == 'true') {
                            swal({
                                title: "Success!",
                                text: "Deleted Successfully!",
                                confirmButtonColor: "#66BB6A",
                                type: "success"
                            }, function () {
                                location.reload();
                            });
                        } else {
                            swal({
                                title: "Something went wrong!",
                                text: "Please Check your Permission's....",
                                confirmButtonColor: "#EF5350",
                                type: "error"
                            });
                        }
                    });
                } else {
                    swal({
                        title: "Cancelled",
                        text: "Course Enquiry not Deleted",
                        confirmButtonColor: "#2196F3",
                        type: "error"
                    });
                }
            });
}