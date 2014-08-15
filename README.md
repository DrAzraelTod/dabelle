# dabelle - sächsisch für Tabelle

## What?

dabelle aims to be for tables what markdown or textile are for text.
Target is to replace the aging CSV and the inherently broken XML-blobs that are used by OpenOffice, LibreOffice, Excel and the likes.

The name comes from the saxonian (east german accent) pronunciation of 'Tabelle', meaning simply 'table'.

to reach it's goals, dabelle-parsers should be able to do two things:

 a) parse simple layouting information and output it into what you want (i.e. HTML, maybe LaTex, XLS, ...)
 b) parse calculation-information and calculate!

Of course part b can be a security-risk, result in infinite loops or otherwise unwanted. Because of this that part is entirely optional.
Every dabelle-b parser should be able to run in a mode where containing data is entirely ignored.

## How?

basically dabelle works similar to CSV, but with some more restrictions:

 - \n for linebreaks
 - UTF-8 only
 - | as field delimeter (why the hell would someone use comma or semikolon? it's something occuring permanently in numeric data)

additional the first symbol in a cell might have special meaning.
Commands that need data (i.e. "merge with N next fields" or "name for this field is X") then that command is closed by the same symbol that started it
unparseable field-content is treated as not containing any commands at all (although an error should be logged)

 - \_ make this field the vertical heading
 - ! make this field the horizontal heading
 - # name for this field, for referencing it later (and making HTML-IDs or similar)
 - & merge with next field, if followed by integer, then merge with next N fields
 - = calculate something, if both field-text and this is aviable, then field-text is only displayed if this doesn't evaluate

### inline/whole-file

two modes to run should be whole-file or inline-modes

in whole file it's asumed that everything in that file is a single table
Those files should be named \*.dabl for obvious reasons.

in inline-mode one file can contain arbitrary numbers of tables
everything outside of tables is ignored (and forwarded to output without change)
tables are started/ended via "\n||table\_name||\n" and "\n||/table\_name||\n"

### Example:

    this is an example text
    it's to be completely ignored by the parser
    
    but the next line starts the first table
    ||table 1||
    _multiply with_!titles|!foo|!bar|!foobar
    _1|foo|bar|foobar
    _2|foofoo|barbar|foobarfoobar
    _3|foofoofoo|barbarbar|foobarfoobarfoobar
    ||/table 1||
    
    this text is ignored again

## Where?

Plan is to write parsers in python and maybe js and/or go.

## When?

...will this work?
It's doen when it's done!

## Legal Foo?

Everyone is free to implement this spec. I would like if you mention where you have the idea from, but you can do whatever you want with it.
One Exception: don't claim that it was your idea!

For code in this repository you have to notice the following (unless stated otherwise right in first lines of the file):

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Dieses Programm ist Freie Software: Sie können es unter den Bedingungen
    der GNU Affero General Public License, wie von der Free Software Foundation,
    Version 3 der Lizenz oder (nach Ihrer Wahl) jeder neueren
    veröffentlichten Version, weiterverbreiten und/oder modifizieren.

    Dieses Programm wird in der Hoffnung, dass es nützlich sein wird, aber
    OHNE JEDE GEWÄHRLEISTUNG, bereitgestellt; sogar ohne die implizite
    Gewährleistung der MARKTFÄHIGKEIT oder EIGNUNG FÜR EINEN BESTIMMTEN ZWECK.
    Siehe die GNU Affero General Public License für weitere Details.

    Sie sollten eine Kopie der GNU Affero General Public License zusammen mit diesem
    Programm erhalten haben. Wenn nicht, siehe <http://www.gnu.org/licenses/>.

### but i don't like copyleft!

Well... go fuck yourself! Copyleft exists for a reason. I like it.

short of that you can always ask me for additional permissions, in most cases i will at least listen to what you tell me. If you have valid reasons i might give you written permission to use it on other terms.
