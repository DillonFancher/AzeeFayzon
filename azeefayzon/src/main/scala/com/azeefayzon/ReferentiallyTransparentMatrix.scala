package com.azeefayzon

class ReferentiallyTransparentMatrix(val rows: Seq[Seq[Long]]) {

  val emptyColumns: Seq[Seq[Long]] = Seq.fill(rows.size)(Seq())
  val columns: Seq[Seq[Long]] = flip(rows, emptyColumns)

  def flip(
    rows: Seq[Seq[Long]],
    columns: Seq[Seq[Long]]
  ): Seq[Seq[Long]] = rows match {
    case Seq() => columns
    case (head: Seq[Long]) :: (tail: Seq[Seq[Long]]) =>
      val zipped = columns.zip(head)
      val newColumns = zipped.map {
        case (col: Seq[Long], n: Long) => col :+ n
      }

      flip(tail, newColumns)
  }

  def transpose(): ReferentiallyTransparentMatrix = {
    new ReferentiallyTransparentMatrix(flip(rows, emptyColumns))
  }

  def get(row: Int, column: Int): Long = {
    rows(row)(column)
  }

  def add(foreignMatrix: ReferentiallyTransparentMatrix): ReferentiallyTransparentMatrix = {
    val newValues = rows.zip(foreignMatrix.rows).map {
      case (us: Seq[Long], them: Seq[Long]) =>
        us.zip(them).map { case (x, y) => x + y }
    }

    new ReferentiallyTransparentMatrix(newValues)
  }

  def multiply(foreignMatrix: ReferentiallyTransparentMatrix): ReferentiallyTransparentMatrix = {
    val newValues = foreignMatrix.columns.map { column =>
      rows.map { row =>
        row.zip(column).map { case (a: Long, b: Long) => a * b }.sum
      }
    }

    val newMatrix = new ReferentiallyTransparentMatrix(newValues)
    newMatrix.transpose()
  }

  override def toString: String = {
    rows.map { rows =>
      val data: String = rows.mkString(" ")
      s"| $data |"
    }.mkString("\n")
  }

}
