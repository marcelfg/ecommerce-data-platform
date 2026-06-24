-- Create the database
CREATE DATABASE olist;

-- Create the schemas
CREATE SCHEMA IF NOT EXISTS olist.raw;
CREATE SCHEMA IF NOT EXISTS olist.staging;
CREATE SCHEMA IF NOT EXISTS olist.intermediate;
CREATE SCHEMA IF NOT EXISTS olist.marts;
CREATE SCHEMA IF NOT EXISTS olist.reference;