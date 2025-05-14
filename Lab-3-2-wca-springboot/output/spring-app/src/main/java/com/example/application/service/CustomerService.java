package com.example.application.service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import com.example.application.model.Customer;
import com.example.application.form.CustomerForm;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class CustomerService {
    private final CustomerRepository customerRepository;

    @Autowired
    public CustomerService(CustomerRepository customerRepository) {
        this.customerRepository = customerRepository;
    }

    @Transactional
    @PreAuthorize("hasRole('ROLE_ADMIN')")
    public Customer saveCustomer(CustomerForm form) {
        Customer customer = new Customer();
        customer.setId(form.getId() != null ? form.getId() : getNextId());
        customer.setName(form.getName());
        customer.setEmail(form.getEmail());
        customer.setPhone(form.getPhone());
        customer.setActive(form.isActive());

        return customerRepository.save(customer);
    }

    @Transactional
    @PreAuthorize("hasRole('ROLE_ADMIN')")
    public void deleteCustomer(Long id) {
        customerRepository.deleteById(id);
    }

    @Transactional
    public CustomerForm getCustomerForm(Long id) {
        Customer customer = customerRepository.findById(id).orElse(null);
        if (customer != null) {
            CustomerForm form = new CustomerForm();
            form.setId(customer.getId());
            form.setName(customer.getName());
            form.setEmail(customer.getEmail());
            form.setPhone(customer.getPhone());
            form.setActive(customer.isActive());
            return form;
        }
        return null;
    }

    @Transactional
    public List<Customer> getAllCustomers() {
        return new ArrayList<>(customerRepository.findAll());
    }

    private long getNextId() {
        long id = 1;
        for (Customer customer : customerRepository.findAll()) {
            if (customer.getId() >= id) {
                id = customer.getId() + 1;
            }
        }
        return id;
    }
}