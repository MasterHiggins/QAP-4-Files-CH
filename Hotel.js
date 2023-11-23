var MotelCustomer = {
    Name: "Chris Higgins",
    BirthDate: "2005-05-22",
    Age: "18",
    Gender: "Male",
    RoomPreferences: ["Non-smoking", "King-size bed"],
    PaymentMethod: "Credit Card",
    MailingAddress: {
      Street: "123 Main St",
      City: "Anytown",
      Province: "NL",
      PostalCode: "A1B2C3",
    },
    PhoneNumber: "709-123-4567",
    CheckInDate: {
        Year: 2023,
        Month: 11,      //Day project started
        Day: 20,
    },
    CheckOutDate: {
        Year: 2023,
        Month: 11,      //Day project ended
        Day: 21,
    },
};

var CustomerDescription = `
  Customer Name: ${MotelCustomer.Name}
  Age: ${MotelCustomer.Age} years old
  Gender: ${MotelCustomer.Gender}
  Room Preferences: ${MotelCustomer.RoomPreferences.join(", ")}
  Payment Method: ${MotelCustomer.PaymentMethod}
  Mailing Address: ${MotelCustomer.MailingAddress.Street}, ${MotelCustomer.MailingAddress.City}, ${MotelCustomer.MailingAddress.Province} ${MotelCustomer.MailingAddress.PostalCode}
  Phone Number: ${MotelCustomer.PhoneNumber}
  Check-in Date: ${MotelCustomer.CheckInDate.Year}-${MotelCustomer.CheckInDate.Month}-${MotelCustomer.CheckInDate.Day}
  Check-out Date: ${MotelCustomer.CheckOutDate.Year}-${MotelCustomer.CheckOutDate.Month}-${MotelCustomer.CheckOutDate.Day}
`;

console.log(CustomerDescription);