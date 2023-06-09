"""test

Revision ID: 6f8f84c22a03
Revises: 6d708f4f79b3
Create Date: 2023-04-21 23:54:37.420515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f8f84c22a03'
down_revision = '6d708f4f79b3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('currency_converter', 'rate')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('currency_converter', sa.Column('rate', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
