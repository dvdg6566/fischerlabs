jQuery(document).ready(function(){
	update = (i,currentVal) => {
		params = {
			'ind':i,
			'currentVal':currentVal
		}
		console.log(params)
		$.post('/changeOrder',params)
		window.setTimeout(() => {
			window.location.reload()
		},50)
	}

// This button will increment the value
	$('[data-quantity="plus1"]').click(function(e){
	// Stop acting like a button
		e.preventDefault();
	// Get the field name
		fieldName = 'quantity1'
	// Get its current value
		var currentVal = parseInt($('input[name='+fieldName+']').val());
	// If is not undefined
		if (!isNaN(currentVal)) {
		// Increment
			$('input[name='+fieldName+']').val(currentVal + 1);
		} else {
			// Otherwise put a 0 there
			$('input[name='+fieldName+']').val(0);
		}
		update(1,currentVal+1)
	});
// This button will decrement the value till 0
$('[data-quantity="minus1"]').click(function(e) {
// Stop acting like a button
	e.preventDefault();
// Get the field name
	fieldName = 'quantity1'
// Get its current value
	var currentVal = parseInt($('input[name='+fieldName+']').val());
// If it isn't undefined or its greater than 0
	if (!isNaN(currentVal) && currentVal > 0) {
	// Decrement one
		$('input[name='+fieldName+']').val(currentVal - 1);
	} else {
	// Otherwise put a 0 there
		$('input[name='+fieldName+']').val(0);
	}
	update(1,currentVal-1)
});
// This button will increment the value
	$('[data-quantity="plus2"]').click(function(e){
	// Stop acting like a button
		e.preventDefault();
	// Get the field name
		fieldName = 'quantity2'
	// Get its current value
		var currentVal = parseInt($('input[name='+fieldName+']').val());
	// If is not undefined
		if (!isNaN(currentVal)) {
		// Increment
			$('input[name='+fieldName+']').val(currentVal + 1);
		} else {
			// Otherwise put a 0 there
			$('input[name='+fieldName+']').val(0);
		}
		update(2,currentVal+1)
	});
// This button will decrement the value till 0
$('[data-quantity="minus2"]').click(function(e) {
// Stop acting like a button
	e.preventDefault();
// Get the field name
	fieldName = 'quantity2'
// Get its current value
	var currentVal = parseInt($('input[name='+fieldName+']').val());
// If it isn't undefined or its greater than 0
	if (!isNaN(currentVal) && currentVal > 0) {
	// Decrement one
		$('input[name='+fieldName+']').val(currentVal - 1);
	} else {
	// Otherwise put a 0 there
		$('input[name='+fieldName+']').val(0);
	}
	update(2,currentVal-1)
});
// This button will increment the value
	$('[data-quantity="plus3"]').click(function(e){
	// Stop acting like a button
		e.preventDefault();
	// Get the field name
		fieldName = 'quantity3'
	// Get its current value
		var currentVal = parseInt($('input[name='+fieldName+']').val());
	// If is not undefined
		if (!isNaN(currentVal)) {
		// Increment
			$('input[name='+fieldName+']').val(currentVal + 1);
		} else {
			// Otherwise put a 0 there
			$('input[name='+fieldName+']').val(0);
		}
		update(3,currentVal+1)
	});
// This button will decrement the value till 0
$('[data-quantity="minus3"]').click(function(e) {
// Stop acting like a button
	e.preventDefault();
// Get the field name
	fieldName = 'quantity3'
// Get its current value
	var currentVal = parseInt($('input[name='+fieldName+']').val());
// If it isn't undefined or its greater than 0
	if (!isNaN(currentVal) && currentVal > 0) {
	// Decrement one
		$('input[name='+fieldName+']').val(currentVal - 1);
	} else {
	// Otherwise put a 0 there
		$('input[name='+fieldName+']').val(0);
	}
	update(3,currentVal-1)
});
// This button will increment the value
	$('[data-quantity="plus4"]').click(function(e){
	// Stop acting like a button
		e.preventDefault();
	// Get the field name
		fieldName = 'quantity4'
	// Get its current value
		var currentVal = parseInt($('input[name='+fieldName+']').val());
	// If is not undefined
		if (!isNaN(currentVal)) {
		// Increment
			$('input[name='+fieldName+']').val(currentVal + 1);
		} else {
			// Otherwise put a 0 there
			$('input[name='+fieldName+']').val(0);
		}
		update(4,currentVal+1)
	});
// This button will decrement the value till 0
$('[data-quantity="minus4"]').click(function(e) {
// Stop acting like a button
	e.preventDefault();
// Get the field name
	fieldName = 'quantity4'
// Get its current value
	var currentVal = parseInt($('input[name='+fieldName+']').val());
// If it isn't undefined or its greater than 0
	if (!isNaN(currentVal) && currentVal > 0) {
	// Decrement one
		$('input[name='+fieldName+']').val(currentVal - 1);
	} else {
	// Otherwise put a 0 there
		$('input[name='+fieldName+']').val(0);
	}
	update(4,currentVal-1)
});
// This button will increment the value
	$('[data-quantity="plus5"]').click(function(e){
	// Stop acting like a button
		e.preventDefault();
	// Get the field name
		fieldName = 'quantity5'
	// Get its current value
		var currentVal = parseInt($('input[name='+fieldName+']').val());
	// If is not undefined
		if (!isNaN(currentVal)) {
		// Increment
			$('input[name='+fieldName+']').val(currentVal + 1);
		} else {
			// Otherwise put a 0 there
			$('input[name='+fieldName+']').val(0);
		}
		update(5,currentVal+1)
	});
// This button will decrement the value till 0
$('[data-quantity="minus5"]').click(function(e) {
// Stop acting like a button
	e.preventDefault();
// Get the field name
	fieldName = 'quantity5'
// Get its current value
	var currentVal = parseInt($('input[name='+fieldName+']').val());
// If it isn't undefined or its greater than 0
	if (!isNaN(currentVal) && currentVal > 0) {
	// Decrement one
		$('input[name='+fieldName+']').val(currentVal - 1);
	} else {
	// Otherwise put a 0 there
		$('input[name='+fieldName+']').val(0);
	}
	update(5,currentVal-1)
});
// This button will increment the value
	$('[data-quantity="plus6"]').click(function(e){
	// Stop acting like a button
		e.preventDefault();
	// Get the field name
		fieldName = 'quantity6'
	// Get its current value
		var currentVal = parseInt($('input[name='+fieldName+']').val());
	// If is not undefined
		if (!isNaN(currentVal)) {
		// Increment
			$('input[name='+fieldName+']').val(currentVal + 1);
		} else {
			// Otherwise put a 0 there
			$('input[name='+fieldName+']').val(0);
		}
		update(6,currentVal+1)
	});
// This button will decrement the value till 0
$('[data-quantity="minus6"]').click(function(e) {
// Stop acting like a button
	e.preventDefault();
// Get the field name
	fieldName = 'quantity6'
// Get its current value
	var currentVal = parseInt($('input[name='+fieldName+']').val());
// If it isn't undefined or its greater than 0
	if (!isNaN(currentVal) && currentVal > 0) {
	// Decrement one
		$('input[name='+fieldName+']').val(currentVal - 1);
	} else {
	// Otherwise put a 0 there
		$('input[name='+fieldName+']').val(0);
	}
	update(6,currentVal-1)
});
// This button will increment the value
	$('[data-quantity="plus7"]').click(function(e){
	// Stop acting like a button
		e.preventDefault();
	// Get the field name
		fieldName = 'quantity7'
	// Get its current value
		var currentVal = parseInt($('input[name='+fieldName+']').val());
	// If is not undefined
		if (!isNaN(currentVal)) {
		// Increment
			$('input[name='+fieldName+']').val(currentVal + 1);
		} else {
			// Otherwise put a 0 there
			$('input[name='+fieldName+']').val(0);
		}
		update(7,currentVal+1)
	});
// This button will decrement the value till 0
$('[data-quantity="minus7"]').click(function(e) {
// Stop acting like a button
	e.preventDefault();
// Get the field name
	fieldName = 'quantity7'
// Get its current value
	var currentVal = parseInt($('input[name='+fieldName+']').val());
// If it isn't undefined or its greater than 0
	if (!isNaN(currentVal) && currentVal > 0) {
	// Decrement one
		$('input[name='+fieldName+']').val(currentVal - 1);
	} else {
	// Otherwise put a 0 there
		$('input[name='+fieldName+']').val(0);
	}
	update(7,currentVal-1)
});
// This button will increment the value
	$('[data-quantity="plus8"]').click(function(e){
	// Stop acting like a button
		e.preventDefault();
	// Get the field name
		fieldName = 'quantity8'
	// Get its current value
		var currentVal = parseInt($('input[name='+fieldName+']').val());
	// If is not undefined
		if (!isNaN(currentVal)) {
		// Increment
			$('input[name='+fieldName+']').val(currentVal + 1);
		} else {
			// Otherwise put a 0 there
			$('input[name='+fieldName+']').val(0);
		}
		update(8,currentVal+1)
	});
// This button will decrement the value till 0
$('[data-quantity="minus8"]').click(function(e) {
// Stop acting like a button
	e.preventDefault();
// Get the field name
	fieldName = 'quantity8'
// Get its current value
	var currentVal = parseInt($('input[name='+fieldName+']').val());
// If it isn't undefined or its greater than 0
	if (!isNaN(currentVal) && currentVal > 0) {
	// Decrement one
		$('input[name='+fieldName+']').val(currentVal - 1);
	} else {
	// Otherwise put a 0 there
		$('input[name='+fieldName+']').val(0);
	}
	update(8,currentVal-1)
});
// This button will increment the value
	$('[data-quantity="plus9"]').click(function(e){
	// Stop acting like a button
		e.preventDefault();
	// Get the field name
		fieldName = 'quantity9'
	// Get its current value
		var currentVal = parseInt($('input[name='+fieldName+']').val());
	// If is not undefined
		if (!isNaN(currentVal)) {
		// Increment
			$('input[name='+fieldName+']').val(currentVal + 1);
		} else {
			// Otherwise put a 0 there
			$('input[name='+fieldName+']').val(0);
		}
		update(9,currentVal+1)
	});
// This button will decrement the value till 0
$('[data-quantity="minus9"]').click(function(e) {
// Stop acting like a button
	e.preventDefault();
// Get the field name
	fieldName = 'quantity9'
// Get its current value
	var currentVal = parseInt($('input[name='+fieldName+']').val());
// If it isn't undefined or its greater than 0
	if (!isNaN(currentVal) && currentVal > 0) {
	// Decrement one
		$('input[name='+fieldName+']').val(currentVal - 1);
	} else {
	// Otherwise put a 0 there
		$('input[name='+fieldName+']').val(0);
	}
	update(9,currentVal-1)
});
});