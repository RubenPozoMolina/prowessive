#!/bin/bash
while ! pg_isready -d postgres -h localhost -p 5432 -U postgres 2>&1 | grep ' accepting connections'
do
  sleep 5
done