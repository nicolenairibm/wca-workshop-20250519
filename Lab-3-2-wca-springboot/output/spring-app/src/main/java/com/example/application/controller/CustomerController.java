package com.example.app.controller;

import javax.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import com.example.app.form.CustomerForm;
import com.example.app.service.CustomerService;

@RestController
@RequestMapping("/customer")
public class CustomerController {
    private CustomerService customerService;

    public CustomerController() {
        customerService = new CustomerService();
    }

    @GetMapping("/list")
    public ResponseEntity<Object> listCustomers() {
        return ResponseEntity.ok(customerService.getAllCustomers());
    }

    @GetMapping("/{id}")
    public ResponseEntity<Object> getCustomer(@PathVariable("id") Long id) {
        CustomerForm customerForm = customerService.getCustomerForm(id);
        if (customerForm == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(customerForm);
    }

    @PostMapping
    public ResponseEntity<Object> createCustomer(@Valid @RequestBody CustomerForm customerForm) {
        customerService.saveCustomer(customerForm);
        return ResponseEntity.status(HttpStatus.CREATED).build();
    }

    @PutMapping("/{id}")
    public ResponseEntity<Object> updateCustomer(@PathVariable("id") Long id,
            @Valid @RequestBody CustomerForm customerForm) {
        if (!id.equals(customerForm.getId())) {
            return ResponseEntity.badRequest().build();
        }
        customerService.saveCustomer(customerForm);
        return ResponseEntity.ok().build();
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Object> deleteCustomer(@PathVariable("id") Long id) {
        customerService.deleteCustomer(id);
        return ResponseEntity.ok().build();
    }
}