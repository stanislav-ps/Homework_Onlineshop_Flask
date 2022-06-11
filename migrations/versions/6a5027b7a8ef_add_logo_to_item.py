"""Add logo to Item

Revision ID: 6a5027b7a8ef
Revises: 5b34dbe02d1a
Create Date: 2022-06-02 12:51:59.212205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a5027b7a8ef'
down_revision = '5b34dbe02d1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('logo', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.drop_column('logo')

    # ### end Alembic commands ###
