#
#     Copyright 2011, Kay Hayen, mailto:kayhayen@gmx.de
#
#     Part of "Nuitka", an optimizing Python compiler that is compatible and
#     integrates with CPython, but also works on its own.
#
#     If you submit Kay Hayen patches to this software in either form, you
#     automatically grant him a copyright assignment to the code, or in the
#     alternative a BSD license to the code, should your jurisdiction prevent
#     this. Obviously it won't affect code that comes to him indirectly or
#     code you don't submit to him.
#
#     This is to reserve my ability to re-license the code at any time, e.g.
#     the PSF. With this version of Nuitka, using it for Closed Source will
#     not be allowed.
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, version 3 of the License.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#     Please leave the whole of this copyright notice intact.
#
""" Templates for the constants handling.

"""

template_constants_reading = """
#include "nuitka/prelude.hpp"

// The current line of code execution.
int _current_line;

// Sentinel PyObject to be used for all our call iterator endings. It will become
// a PyCObject pointing to NULL. TODO: Hopefully that is unique enough.
PyObject *_sentinel_value = NULL;

PyModuleObject *_module_builtin = NULL;

%(constant_declarations)s

void _initConstants( void )
{
    if ( _sentinel_value == NULL )
    {
        _sentinel_value = PyCObject_FromVoidPtr( NULL, NULL );
        assert( _sentinel_value );

        _module_builtin = (PyModuleObject *)PyImport_ImportModule( "__builtin__" );
        assert( _module_builtin );

        UNSTREAM_INIT();

%(constant_inits)s
    }
}
"""

template_constants_declaration = """\
// Call this to initialize all of the below
void _initConstants( void );

%(constant_declarations)s
"""