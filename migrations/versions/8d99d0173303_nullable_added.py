"""nullable added

Revision ID: 8d99d0173303
Revises: 8ecf2aeecf4a
Create Date: 2023-04-21 21:39:15.603682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d99d0173303'
down_revision = '8ecf2aeecf4a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('currency_converter', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('currency_converter', 'code',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('currency_converter', 'rate',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('currency_converter', 'rate',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('currency_converter', 'code',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('currency_converter', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
