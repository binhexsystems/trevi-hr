##############################################################################
#
#    Copyright (C) 2013 Michael Telahun Makonnen <mmakonnen@gmail.com>.
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Employee Seniority",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "TREVI Software",
    "category": "Human Resources",
    "summary": "Calculate an employee's months of employment",
    "website": "https://github.com/trevi-software/trevi-hr",
    "depends": [
        "hr_contract",
    ],
    "data": [
        "views/hr_view.xml",
    ],
    "demo": [],
    "installable": True,
}
