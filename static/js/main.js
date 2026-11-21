document.addEventListener("DOMContentLoaded", function () {
  const passengerSelect = document.getElementById("passengers");
  if (!passengerSelect) return;

  const farePerPassenger = Number(passengerSelect.dataset.fare || 0);
  const passengerCount = document.getElementById("passenger-count");
  const baseTotal = document.getElementById("base-total");
  const taxTotal = document.getElementById("tax-total");
  const grandTotal = document.getElementById("grand-total");
  const formatRupees = amount => "₹" + amount.toLocaleString("en-IN");

  function updatePrice() {
    const people = Number(passengerSelect.value);
    const fare = farePerPassenger * people;
    const taxes = 350 * people;
    passengerCount.textContent = people;
    baseTotal.textContent = formatRupees(fare);
    taxTotal.textContent = formatRupees(taxes);
    grandTotal.textContent = formatRupees(fare + taxes);
  }

  passengerSelect.addEventListener("change", updatePrice);
  updatePrice();
});
